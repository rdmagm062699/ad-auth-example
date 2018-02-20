from flask import Blueprint, redirect, url_for, session, request, render_template
from jose import jws
import json, requests, uuid, yaml
from app.mod_auth.security.microsoft_client import microsoft_client
from app.mod_auth.security.user_operations import get_user
from app import app, config

mod_auth = Blueprint('auth', __name__)
microsoft = microsoft_client(config, mod_auth)

@mod_auth.route('/')
@mod_auth.route('/login', methods = ['POST', 'GET'])
def login():
    if 'microsoft_token' in session:
        return redirect(url_for('auth.me'))

    return _authenticate(session, microsoft)

@mod_auth.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('microsoft_token', None)
    session.pop('claims', None)
    session.pop('state', None)
    return redirect(url_for('auth.login'))

@mod_auth.route('/login/authorized')
def authorized():
    _verify_state(session, request)
    response = microsoft.authorized_response()

    if response is None:
        return _access_denied_message(response)

    _store_results(session, response)
    return redirect(url_for('auth.me'))

@mod_auth.route('/me')
def me():
    me = microsoft.get('me')
    data={'$select':config['user_attributes'], '$expand':'extensions'}
    user_identity = microsoft.get('me', data=data)

    return render_template('auth/me.html', me=str(me.data), user_identity=user_identity.data)

# If library is having trouble with refresh, uncomment below and implement refresh handler
# see https://github.com/lepture/flask-oauthlib/issues/160 for instructions on how to do this
# Implements refresh token logic
# @app.route('/refresh', methods=['POST'])
# def refresh():

@microsoft.tokengetter
def get_microsoft_oauth_token():
    return session.get('microsoft_token')

def _authenticate(session, microsoft_client):
    session['state'] = uuid.uuid4()
    return microsoft_client.authorize(callback=url_for('auth.authorized', _external=True), state=session['state'])

def _access_denied_message(request):
    return "Access Denied: Reason=%s\nError=%s" % (response.get('error'), request.get('error_description'))

def _verify_state(session, request):
    if str(session['state']) != str(request.args['state']):
        raise Exception('State has been tampered with, end authentication')

def _store_results(session, response):
    access_token = response['access_token']
    session['microsoft_token'] = (access_token, '')

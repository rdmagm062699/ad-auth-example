from flask import Blueprint, redirect, url_for, session, request, render_template
from flask_login import login_required, login_user, login_required, logout_user, current_user
from app.mod_auth.security.microsoft_client import microsoft_client
from app.mod_auth.security.user import User
from app import app, config, login_manager
import uuid

mod_auth = Blueprint('auth', __name__)
microsoft = microsoft_client(config, mod_auth)

@mod_auth.route('/')
def route_to_list():
    return redirect(url_for('b2c_mgmt.my_caregivers'))

@mod_auth.route('/login', methods = ['POST', 'GET'])
def login():
    if 'microsoft_token' in session:
        return redirect(url_for('b2c_mgmt.my_caregivers'))
    session['_flashes'] = [] # Bad way to clear unnecessary flashed messages for authentication
    return _authenticate(session, microsoft)

@mod_auth.route('/logout', methods = ['POST', 'GET'])
@login_required
def logout():
    session.pop('state', None)
    session.pop('access_token', None)
    logout_user()
    return redirect(url_for('auth.login'))

@mod_auth.route('/login/authorized')
def authorized():
    _verify_state(session, request)
    response = microsoft.authorized_response()

    if response is None:
        return abort(401)

    session['access_token'] = response['access_token']
    login_user(_user())
    return redirect(url_for('b2c_mgmt.my_caregivers'))

@mod_auth.route('/me')
@login_required
def me():
    return render_template('auth/me.html', user_identity=current_user.data())

# If library is having trouble with refresh, uncomment below and implement refresh handler
# see https://github.com/lepture/flask-oauthlib/issues/160 for instructions on how to do this
# Implements refresh token logic
# @app.route('/refresh', methods=['POST'])
# def refresh():

@microsoft.tokengetter
def get_microsoft_oauth_token():
    return (session['access_token'], '')

@login_manager.user_loader
def load_user(user_id):
    user = _user()
    if user_id == user.get_id():
        return user
    return None

def _authenticate(session, microsoft_client):
    session['state'] = uuid.uuid4()
    return microsoft_client.authorize(callback=url_for('auth.authorized', _external=True), state=session['state'])

def _verify_state(session, request):
    if str(session['state']) != str(request.args['state']):
        raise Exception('State has been tampered with, end authentication')

def _user():
    data={'$select':config['user_attributes'], '$expand':'extensions'}
    return User(microsoft.get('me', data=data).data)

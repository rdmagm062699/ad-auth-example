from flask_oauthlib.client import OAuth, OAuthException
import json, requests

def microsoft_client(config, app):
    return OAuth(app).remote_app(
        'microsoft',
        consumer_key=config['client_id'],
        consumer_secret=config['client_secret'],
        request_token_params={'scope': 'offline_access User.Read' },
        base_url=config['microsoft_graph_api_url'],
        request_token_url=None,
        access_token_method='POST',
        access_token_url=_token_url(config),
        authorize_url=_authorize_url(config)
    )

def _core_url():
    return 'https://login.microsoftonline.com/common/'

def _token_url(config):
    return _core_url() + '/oauth2/v2.0/token'

def _authorize_url(config):
    return _core_url() + '/oauth2/v2.0/authorize'

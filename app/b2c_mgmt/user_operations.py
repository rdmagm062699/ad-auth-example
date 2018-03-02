from requests.auth import HTTPBasicAuth
import urllib3 # This is only due to spike having self-signed cert.
import string, json, requests

class UserOperations:
    def __init__(self, config):
        # We should do client_secret_post
        # or some other option then client_secret_basic
        # this is also using test SCIM instead of UMA
        self.config = config

    def users(self):
        self._disable_self_signed_cert_warnings()
        headers = {'Authorization': self._auth_token(self.config)}
        data = {'count': 100}
        result = requests.get(self._user_endpoint(self.config), headers=headers, data=data, verify=False).text # this is spike so cert is self-signed
        return json.loads(result)['Resources']

    def _token(self, config):
        auth = HTTPBasicAuth(config['iam_client_id'], config['iam_client_secret'])
        data = {'grant_type':'client_credentials'}
        result = requests.post(self._token_endpoint(config), auth=auth, data=data, verify=False).text # this is spike so cert is self-signed
        return json.loads(result)

    def _disable_self_signed_cert_warnings(self):
        urllib3.disable_warnings()

    def _token_endpoint(self, config):
        return config['iam_server_url'] + '/oxauth/restv1/token'

    def _user_endpoint(self, config):
        return config['iam_server_url'] + '/identity/restv1/scim/v2/Users'

    def _auth_token(self, config):
        token = self._token(config)
        return 'Bearer %s' % self._token(config)['access_token']

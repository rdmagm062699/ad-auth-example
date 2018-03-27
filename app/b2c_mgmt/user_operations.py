from requests.auth import HTTPBasicAuth
import urllib3, urllib # This is only due to spike having self-signed cert.
import string, json, requests

def pretty_print(req):
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

class UserOperations:
    def __init__(self, config):
        # We should do client_secret_post
        # or some other option then client_secret_basic
        # this is also using SCIM Test Mode instead of UMA 2.0
        self.config = config

    def users(self, franchises=['100']): # we are going to default all requests to a list containing franchise 100 for now.
        self._disable_self_signed_cert_warnings() # We are using a self signed cert on our Gluu test server for this spike.
        headers = {'Authorization': self._auth_token(self.config)}
        data = {'filter': self._franchise_filter(franchises), 'startIndex': 1, 'count': 100}
        result = requests.get(self._user_endpoint(self.config), headers=headers, params=data, verify=False).text # this is spike so cert is self-signed so don't verify
        return json.loads(result)['Resources']

    def create_user(self, first_name, last_name, email, franchise_number):
        headers = {'Authorization': self._auth_token(self.config), 'Content-Type': 'application/scim+json' }
        data = self._create_caregiver_data(first_name, last_name, email, franchise_number, self.config['iam_default_password'])
        result = requests.post(self._user_endpoint(self.config), headers=headers, data=data, verify=False)
        print(result)
        return json.loads(result.text)['Resources']

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

    def _franchise_filter(self, franchises):
        if franchises:
            filters = ['franchises eq "{}"'.format(franchise) for franchise in franchises]
            return ' or '.join(filters)
        return ''

    def _create_caregiver_data(self, first_name, last_name, email, franchise_number, password):
        return {
            'schemas': ['urn:ietf:params:scim:schemas:extension:gluu:2.0:User','urn:ietf:params:scim:schemas:core:2.0:User'],
            'userName': email,
            'name': {
                'familyName': last_name,
                'givenName': first_name
            },
            'displayName': first_name + ' ' + last_name,
            'emails': [{
                'value': email,
                'type': 'work',
                'primary': 'true'
            }],
            'password': password,
            'groups': 'CAREGiver'#,
            #'franchises': [franchise_number]
        }

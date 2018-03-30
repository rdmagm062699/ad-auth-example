from okta import UsersClient
from okta.framework.ApiClient import ApiClient #UsersClient does not support all attributes especially custom attribtues
# May want to consider just dropping to our own client OR supply a patch to theirs that improves their python client.
import string, json, requests, urllib.parse

class UserOperations:
    def __init__(self, config):
        self.config = config
        self.user_client = UsersClient(self.config['iam_server_url'], self.config['iam_client_secret'])
        self.api_client = ApiClient(base_url=self.config['iam_server_url'], api_token=self.config['iam_client_secret'], pathname='/api/v1/users')

    def users(self, franchises=['100']): # we are going to default all requests to a list containing franchise 100 for now.
        url_path='?'+self._franchise_filter(franchises)
        return json.loads(self.api_client.get_path(url_path=url_path).text) # No paging handled here!  Would need to do that in real implementation

    def create_user(self, first_name, last_name, email, franchise_number):
        user = self._create_caregiver_data(first_name=first_name, last_name=last_name, email=email, franchise_number=franchise_number)
        return self.user_client.create_user(user=user, activate=True)

    def _franchise_filter(self, franchises):
        # Needed to deal with url_encoding problems that the ApiClient/UserClient doesn't handle.
        if franchises:
            filters = ['profile.franchises eq "{}"'.format(franchise) for franchise in franchises]
            query = {'search': ' or '.join(filters)}
            return urllib.parse.urlencode(query, quote_via=urllib.parse.quote)
        return ''

    def _create_caregiver_data(self, first_name, last_name, email, franchise_number):
        return {
            'profile': {
                'lastName': last_name,
                'firstName': first_name,
                'email': email,
                'login': email,
                'franchises': [franchise_number]
            },
            'credentials': {
                'password': { 'value': self.config['iam_default_password'] }
            },
            'groupIds': self.config['iam_default_caregiver_group_ids']
        }

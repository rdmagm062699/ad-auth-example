from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import ServicePrincipalCredentials
import string, json

def b2c_user(email, config):
    filterTemplate=string.Template("otherMails/any(c:c eq '$email')")
    filter = filterTemplate.substitute(email=email)
    user = next(_client(config).users.list(filter=filter), None)
    return json.dumps(_convert_user(user), indent=4, sort_keys=True)

def b2c_users(config):
    return [_convert_user(user) for user in _client(config).users.list()]

def _convert_user(user):
    if user:
        user.enable_additional_properties_sending()
        return user.serialize()
    return None

def _client(config):
	return GraphRbacManagementClient(_credentials(config), config['graph_tenant_id'])

def _credentials(config):
	return ServicePrincipalCredentials(
        client_id=config['graph_client_id'],
        secret=config['graph_client_secret'],
        tenant=config['graph_tenant_id'],
        resource=config['ad_graph_url'])

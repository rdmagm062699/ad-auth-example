from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.graphrbac.models import PasswordProfile, SignInName
from app.b2c_mgmt.user.hisc_user_create_parameters import HISCUserCreateParameters
import click
import yaml


def _create_user(config, first_name, last_name, email):
    client = _client(config)
    user = client.users.create(_user_create_parameters(first_name, last_name, email, config))
    return user.serialize()


def _client(config):
    return GraphRbacManagementClient(_credentials(config), config['graph_tenant_id'])


def _credentials(config):
    return ServicePrincipalCredentials(
        client_id=config['graph_client_id'],
        secret=config['graph_client_secret'],
        tenant=config['graph_tenant_id'],
        resource=config['ad_graph_url'])


def _user_create_parameters(first_name, last_name, email, config):
    return HISCUserCreateParameters(
        account_enabled=True,
        display_name='{}.{}'.format(first_name, last_name),
        password_profile=_password_profile(config),
        user_principal_name=_principle_name(email, config),
        mail_nickname=_mail_nickname(email),
        given_name=first_name,
        surname=last_name,
        user_type='Guest',
        other_mails=[email],
        sign_in_names=[_sign_in_name(email)],
        usage_location='US',
        creation_type='LocalAccount'
    )


def _password_profile(config):
    return PasswordProfile(password=config['default_password'], force_change_password_next_login=True)


def _principle_name(email, config):
    return config['principle_template'].format(_mail_nickname(email))


def _mail_nickname(email):
    return '{}#EXT#'.format(_format_email(email))


def _format_email(email):
    return email.replace('@', '_')


def _sign_in_name(email):
    return SignInName(type='emailAddress', value=email)


@click.command()
@click.argument('first_name')
@click.argument('last_name')
@click.argument('email')
def create(first_name, last_name, email):
    with open("config/config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)

    result = _create_user(config, first_name, last_name, email)
    print(result)


if __name__ == "__main__":
    create()
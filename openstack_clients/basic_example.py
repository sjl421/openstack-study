from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client

from novaclient import client as nova_clinet
from cinderclient import client as cinder_client
from novaclient import client as neutron_client

auth = v3.Password(
    user_domain_name="Default",
    auth_url='http://controller:35357/v3',
    username='admin',
    password='password',
    project_id='## admin's project id here ##')
session = session.Session(auth=auth)

keystone = keystone_client.Client(session=session)
print(keystone)

nova = nova_clinet.Client(version=2, session=session)
print(nova)

cinder = cinder_client.Client(version=2, session=session)
print(cinder)

neutron = neutron_client.Client(version=2, session=session)
print(neutron)


# coding: utf-8

# In[106]:

import sys
import json

from collections import defaultdict
from keystoneclient.v3 import client as keystone_client
from novaclient import client as novac
from neutronclient.v2_0 import client as neuc


# In[107]:

c = keystone_client.Client(
    user_domain_name="Default",
    username="admin",
    password="password",
    auth_url="http://192.168.56.200:35357/v3",
    tenant_id="b1b5152f6ab24472a99e6a9095b0244e",
)
TOKEN = c.auth_token
print(TOKEN)


# In[108]:

nova = novac.Client("2.37", "admin", "password", "b1b5152f6ab24472a99e6a9095b0244e",
                     "http://192.168.56.200:35357/v3", user_domain_name="Default")
neutron = neuc.Client(endpoint_url='http://192.168.56.200:9696/', token=TOKEN)


# In[109]:

nova.glance.list()[0].id


# In[110]:

nova.flavors.list()[0].id


# In[111]:

nics = [{"net-id": neutron.list_networks()["networks"][0]["id"]}]
print (nics)


# In[122]:

r = nova.servers.create(
    "test",
    nova.glance.list()[0].id,
    nova.flavors.list()[0].id,
    nics=nics
)
print("%s is created" % r.name)


# In[117]:

for s in nova.servers.list():
    print (s.name, s.id)
    nova.servers.delete(s.id)


# In[ ]:




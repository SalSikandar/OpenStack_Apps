import os
#https://docs.openstack.org/user-guide/sdk-neutron-apis.html#create-network
#The examples in this section use the get_credentials method:
#This code resides in the credentials.py file, which all samples import.
#Use the get_credentials() method to populate and get a dictionary:
#credentials = get_credentials()
def get_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

#The examples in this section use the get_nova_credentials method:
#This code resides in the credentials.py file, which all samples import.
#Use the get_nova_credentials() method to populate and get a dictionary:
#nova_credentials = get_nova_credentials()

def get_nova_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

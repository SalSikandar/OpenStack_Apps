#!/usr/bin/env python
from neutronclient.v2_0 import client
from credentials import get_credentials
import json


#network_name = 'sample_network'
#credentials = get_credentials()
#neutron = client.Client(**credentials)
#try:
#    body_sample = {'network': {'name': network_name,
#                   'admin_state_up': True}}

#    netw = neutron.create_network(body=body_sample)
#    net_dict = netw['network']
#    network_id = net_dict['id']
#    print('Network %s created' % network_id)

#    body_create_subnet = {'subnets': [{'cidr': '192.168.199.0/24',
#                          'ip_version': 4, 'network_id': network_id}]}

#    subnet = neutron.create_subnet(body=body_create_subnet)
#    print('Created subnet %s' % subnet)
#finally:
#    print("Execution completed")

credentials = get_credentials()
neutron = client.Client(**credentials)

#netw = neutron.create_network({'network':
#				{'name' : 'salmans',
#				'admin_state_up': True}
#				})

network_list_json = neutron.list_networks()
#print json.dumps (network_list_json, indent=4, sort_keys=True)

##Writing the list of networks to a json for easy parsing
with open ('network_list', 'w') as outfile:
	json.dump(network_list_json, outfile, indent=4)

#if 'id' in network_list_json ['network']:
#	network_list_json ['network'['id']]
#else:
#	print ('No networks exist')

print 'networks' in network_list_json
print network_list_json ['networks']

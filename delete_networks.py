#!/usr/bin/env python
from neutronclient.v2_0 import client
from credentials import get_credentials
import json
import time

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

#This gives the total number of networks
number_of_networks = len(network_list_json["networks"])
#print number_of_networks


#print (network_list_json["networks"][0]["id"])
#print (network_list_json["networks"][0]["router:external"])
#print (network_list_json["networks"][1]["id"])
#print (network_list_json["networks"][1]["router:external"])

#neutron.delete_network(network_list_json["networks"][1]["id"])
#print (network_list_json["networks"][2]["id"])
#print (network_list_json["networks"][2]["router:external"])

#neutron.delete_network(network_list_json["networks"][2]["id"])
#print (network_list_json["networks"][3]["id"])
#print (network_list_json["networks"][3]["router:external"])

#neutron.delete_network(network_list_json["networks"][0]["id"])
#time.sleep(30)
for x in range (0,number_of_networks):
	#print x
	print "THE ID OF THIS NETWORK IS:"
	print (network_list_json["networks"][x]["id"])
	if network_list_json["networks"][x]["router:external"] == False:
		print "THIS IS A PRIVATE NETWORK"
		print "====DELETING===="
		neutron.delete_network (network_list_json["networks"][x]["id"])
	elif network_list_json["networks"][x]["router:external"] == True:
		print "THIS IS A PUBLIC NETWORK"
		print "SKIPPING DELETION" 




#for x in range (0,number_of_networks-1):
#     print x
#     neutron.delete_network(network_list_json["networks"][0]["id"])

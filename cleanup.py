from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

auth_username = 'facebook10210657617530190'
auth_password = 'H9BBS15ili4bn2gf'
auth_url = 'http://8.43.86.2:5000'
project_name = 'facebook10210657617530190'
region_name = 'RegionOne'

provider = get_driver(Provider.OPENSTACK)
conn = provider(auth_username,
                auth_password,
                ex_force_auth_url=auth_url,
                ex_force_auth_version='2.0_password',
                ex_tenant_name=project_name,
                ex_force_service_region=region_name)

##LISTING ALL IMAGES
print ("ALL IMAGES AVAILABLE")
print ("########################")
images = conn.list_images()
for image in images:
 print (image)

##LISTING ALL FLAVORS
print ("  ")
print ("ALL FLAVORS AVAILABLE")
print ("#######################")
flavors = conn.list_sizes()
for flavor in flavors:
 print (flavor)

##Get an image of your choice
print ("  ")
print ("SELECTED IMAGE")
print ("######################")
image_id = '76f5f4aa-a78f-4703-b738-cab967957431'
image = conn.get_image(image_id)
print (image)

#Get a flavor of your choice
print (" ")
print ("SELECTED FLAVOR")
print ("#####################")
flavor_id = '1'
flavor = conn.ex_get_size(flavor_id)
print (flavor)


##Listing existing instances
print (" ")
print ("Listing all running instances")
print ("#################")
instances = conn.list_nodes()
for instance in instances:
  print (instance)


#Deleting all instances
print ("")
print ("Deleting all instances")
print ("#################")
instances = conn.list_nodes()
for instance in instances:
  print ("Deleting ")
  print (instance)
  conn.destroy_node(instance)

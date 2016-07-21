import os
import netifaces

def interfaces():
    interf = netifaces.interfaces()
    list = {}
    for address in interf:
        if netifaces.AF_INET in netifaces.ifaddresses(address):
            for link in netifaces.ifaddresses(address)[netifaces.AF_INET]:
                #print "Interface: " + address + " ,IP: " + link['addr'] + " , Mask: " + link['netmask']
                #iplist.append(link['addr'])
                #iflist.append(address)
                list[address] = link['addr']
    return list
'''
os.system("clear")
print "Network interfaces & IPs"
print "------------------------"
for i in interfaces():
    print "Interface name: ",i,", IP: ",interfaces()[i]
'''
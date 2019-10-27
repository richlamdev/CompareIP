#!/bin/usr/python
#
# Richard Lam, October 2019
#
# Simple script to generate full list of IP's for a given CIDR network
#
# Replace the CIDR network below.  Output to STOUT and to file.
#
# If an error similar to:
# ValueError: 192.168.0.0/8 has host bits set
# Is likely due to inappropriate incorrect CIDR class size
#
# Written for Python 3

import re
import ipaddress

net = ipaddress.ip_network("192.168.1.0/24")

for ip in net:
    print(ip)

netfilename = re.sub ("\/", "_", str(net))

print ("")
print ("File created:")
print (netfilename + ".txt")

with open(netfilename + ".txt","w",newline='\n') as ip_file:
    for ip in net:
       print(ip, sep='', file=ip_file)

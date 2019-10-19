#!/bin/usr/python

# Richard Lam, October 2019
#
# Script to compare IP's from two separate files.  Delimited (separated) by newline (\n)

import sys
import ipaddress

argc = len(sys.argv)

if argc < 3:
    print ("")
    print ("Usage: python3 compare_ip_lists.py <input file one>  <input file two>")
    print ("")
    print ("")
    print ("File Format:")
    print ("IP's listed in file, one per line.")
    print ("192.168.1.1")
    print ("192.168.2.3")
    print ("10.255.2.5")
    print ("172.16.8.8")
    print ("")
    print ("Notes: 1) Duplicate entries within same file are deduplicated.")
    print ("       2) IP addresses are checked for validity.")
    print ("       3) IP addresses are sorted on output and identical to file.")
    print ("")
    sys.exit()
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

# Read in the files, and sort list
with open(file1, 'r') as list1:
    lista = list1.readlines()
with open(file2, 'r') as list2:
    listb = list2.readlines()

comm = set(lista).intersection(listb)
common = sorted(ipaddress.ip_address(line.strip()) for line in comm)

diffa = list(set(lista) - set(listb))
differencea = sorted(ipaddress.ip_address(line.strip()) for line in diffa)

diffb = list(set(listb) - set(lista))
differenceb = sorted(ipaddress.ip_address(line.strip()) for line in diffb)

print ("")
print ("IP's in both files:")
print(*common, sep = "\n")
print ("")
print ("IP's only in: " + file1 )
print(*differencea, sep = "\n")
print ("")
print ("IP's only in: " + file2 )
print(*differenceb, sep = "\n")

with open(file1 + "_" + file2 + "_common_ips","w",newline='\n') as common_file:
    for ip in common:
        print(ip, sep='', file=common_file)

with open(file1 + "_" + file2 + "_ips_only_in_" + file1,"w",newline='\n') as diff_filea:
    for ip in differencea:
        print(ip, sep='', file=diff_filea)

with open(file1 + "_" + file2 + "_ips_only_in_" + file2,"w",newline='\n') as diff_fileb:
    for ip in differenceb:
        print(ip, sep='', file=diff_fileb)

print ("")
print ("Files created:")
print (file1 + "_" + file2 + "_common_ips")
print (file1 + "_" + file2 + "_ips_only_in_" + file1)
print (file1 + "_" + file2 + "_ips_only_in_" + file2)

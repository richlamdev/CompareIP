#!/bin/usr/python
#
# Richard Lam, October 2019
# Rewritten with argparse March 2019
#
# Script to compare IP's from two separate files.  
# Delimited (separated) by newline (\n)
# 
# Written for Python 3

import sys
import ipaddress
import argparse

def compare_files(args):

    file1 = args.first_list.name
    file2 = args.second_list.name

    with args.first_list as firstfile:
        lista = [line.rstrip() for line in firstfile]

    with args.second_list as secondfile:
        listb = [line.rstrip() for line in secondfile]

    # determine common IP's between files
    comm = set(lista) & set(listb)
    common = sorted(ipaddress.ip_address(line.strip()) for line in comm)

    # determine IP's only in first file
    diffa = set(lista) - set(listb)
    differencea = sorted(ipaddress.ip_address(line.strip()) for line in diffa)

    # determine IP's only in second file
    diffb = set(listb) - set(lista)
    differenceb = sorted(ipaddress.ip_address(line.strip()) for line in diffb)

    print ()
    print ("IP's common to " + file1 + " and " + file2)
    print(*common, sep = "\n")
    print ()
    print ("IP's only in: " + file1 )
    print(*differencea, sep = "\n")
    print ()
    print ("IP's only in: " + file2 )
    print(*differenceb, sep = "\n")

    with open(file1 + "_" + file2 + "_ips_common.txt","w") as common_file:
        for ip in common:
            print(ip, sep='', file=common_file)

    with open(file1 + "_" + file2 + "_ips_only_in_" + file1,"w") as diff_filea:
        for ip in differencea:
            print(ip, sep='', file=diff_filea)

    with open(file1 + "_" + file2 + "_ips_only_in_" + file2,"w") as diff_fileb:
        for ip in differenceb:
            print(ip, sep='', file=diff_fileb)

    print ()
    print ("Files created:")
    print (file1 + "_" + file2 + "_ips_common.txt")
    print (file1 + "_" + file2 + "_ips_only_in_" + file1)
    print (file1 + "_" + file2 + "_ips_only_in_" + file2)

def main():
    parser = argparse.ArgumentParser (add_help=True,
             description="Compares two lists of IP's.\n\n\
Output: IP's common to both files.  IP's must be valid format.\n\
        IP's exclusive to the first file.\n\
        IP's exclusive to the second file.", 
    formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('first_list', type=argparse.FileType('r'),
                        metavar="<first file>", help="list of ip's, Format: one IP per line.")

    parser.add_argument('second_list', type=argparse.FileType('r'),
                        metavar="<second file>", help="list of ip's, Format: one IP per line.")

    args = parser.parse_args()

    compare_files (args)

if __name__ == "__main__":
    main()

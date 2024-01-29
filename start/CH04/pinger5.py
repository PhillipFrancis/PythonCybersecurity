#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By Phillip Francis 1/27

import os
import platform
dir_path = os.path.dirname(os.path.realpath(__file__))

def ping_address(ip_address):
    # find our OS
    current_os = platform.system().lower()
    if current_os == "windows":
        # Build our ping command for windows
        ping_cmd = "ping -n 1 -w 1000 {0} > nul".format(ip_address)
    else:
        # build ping command if linux
        ping_cmd = "ping  -c 1 -w 1 {0} > /dev/null 2>1&".format(ip_address)
    # Execute the ping command
    exit_code = os.system(ping_cmd)
    if exit_code == 0:
        return True
    return False

# open file for readin

f = open(dir_path + "/ips.txt", "r")
# Read file Contents
ip_addresses = f.readlines()
# close File
f.close()
# loop file
for ip_address in ip_addresses:
    
    #clean up ip address
    ip_address = ip_address.strip()
    
    #CALL FUNCTION
    result = ping_address(ip_address)

    # print out results
    if result :
        print("{0} is online".format(ip_address))
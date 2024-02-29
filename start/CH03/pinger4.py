#!/usr/bin/env python3
# Fourth example of pinging from Python
# By Phillip Francis 1/19

import os
import platform

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


# Assign ip address to Variable
ip_prefix = '192.168.0.'
# for loop for 1-255
for octet in range(255):
    #setup ip address
    ip_address = ip_prefix + str(octet + 1)

    #CALL FUNTION
    result = ping_address(ip_address)

    # print out results
    if result :
        print("{0} is online".format(ip_address))
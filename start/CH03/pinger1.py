#!/usr/bin/env python3
# First example of pinging from Python
# By Phillip Francis 1/19


import os

# Assign ip address to Variable
ip_address = '127.0.0.1'
# Build our ping command
ping_cmd = "ping  -c 1 -w 1 {0} > /dev/null 2>1& .format(ip_address)
# Execute the ping command
exit_code = os.system(ping_cmd)
# print out results
print(exit_code)

#!/usr/bin/env python3
# Second example of pinging from Python
# By Phillip 1/19

import os
import platform

# Assign ip address to Variable
ip_address = '127.0.0.1'
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
# print out results
print(exit_code)
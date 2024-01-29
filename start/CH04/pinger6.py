#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By Phillip Francis 1/27

import os
import platform
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

def write_log(message):
    # Get the Current Time
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n" 
    # Open a log file for appending
    f = open(dir_path + "/pinger.log", "a")    
    #write message with date and time
    f.write(message)
    #close file
    f.close
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

# open file for reading

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
        write_log("{0} is online".format(ip_address))
    else:
        write_log("{0} is offline".format(ip_address))
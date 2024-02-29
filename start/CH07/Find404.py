#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Phillip Francis 2/22/24    

import os
#Prompt for file and open
log_file = input("which file do you want to scan")
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/access.log", "r")

#readfile and open
while True:
    line = f.readline() 
    if not line:
        break
    #Find 404 error codes
#    if "404" in line:
 #       print(line.strip())
    
    #search for a certain ip address that has a 404 error code
    if "ip" in line:
        if "404" in line:
            print(line.strip())
   

#close file
f.close()

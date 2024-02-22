#!/usr/bin/env python3
# Script that scans web server logs for possible hacking
# Use RegEx to find and report on common hacking types
# Based on https://www.cgisecurity.com/fingerprinting-port80-attacks-a-look-into-web-server-and-web-application-attack-signatures-part-two.html
# By 


import os
import re


# Prompt for file and open
log_file = input("which file do you want to scan")
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/access.log", "r")
log_lines = f.readlines()
f.close()

# Setup RegEx patterns
find_wildcard_uri_pattern = r'\"(\S+)\s(\S*\*\S*)\s*(\S+)\"'
find_backtick_uri_pattern = r'\"(\S+)\s(\S*`\*\S*)\s*(\S+)\"'
find_code_uri_pattern = r']\s\"(\S+)\s(\S*[\^\[\]#{}\"]\S*)\s*(\S+)\"'
find_css_uri_pattern = r']\s\"(\S+)\s(\S*[\(\)]\S*)\s*(\S+)\"'
find_foldertraversal_uri_pattern = r']\s\"(\S+)\s(\S*///\S*)\s*(\S+)\"'

for line in log_lines:
    m = re.search(find_wildcard_uri_pattern, line)
    if m:
        print("Possible attack: Wilcard in URI") 
        print("\t{0}".format(line.strip()))
    m = re.search(find_backtick_uri_pattern, line)
    if m:
        print("Possible attack: Backtick in URI") 
        print("\t{0}".format(line.strip()))
    m = re.search(find_code_uri_pattern, line)
    if m:
        print("Possible attack: Code in URI") 
        print("\t{0}".format(line.strip()))
    m = re.search(find_css_uri_pattern, line)
    if m:
        print("Possible attack: CSS in URI") 
        print("\t{0}".format(line.strip()))
    m = re.search(find_foldertraversal_uri_pattern, line)
    if m:
        print("Possible attack: Folder Traversal in URI") 
        print("\t{0}".format(line.strip()))
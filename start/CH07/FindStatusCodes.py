#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Phillip Francis 2/22/24    

import os
# Import regular expressions
import re

# Prompt for file and open
log_file = input("which file do you want to scan")
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/access.log", "r")
log_lines = f.readlines()
f.close()

# Set up the regex pattern and dictionary
regex_pattern = r"\s(\d{3})\s"
result_dictionary = {}

# find match in file and store in dictionary
for line in log_lines:
    # Search for the pattern, if found, store it
    m = re.search(regex_pattern, line)
    if m:
        status_code = m.group()
        #store status in dictionary
        if status_code in result_dictionary.keys():
            result_dictionary[status_code] += 1
        else:
            result_dictionary[status_code] = 1

# print(result_dictionary)


#   sort and print most frequent result. 
# for key in result_dictionary.keys():
#    print("{0} - {1}".format(key, result_dictionary[key]))

# sort by the most common result

for w in sorted(result_dictionary, key=result_dictionary.get, reverse=True):
    print(w, result_dictionary[w])
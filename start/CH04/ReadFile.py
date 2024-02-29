#!/usr/bin/env python3
# Sample script that reads from a file
# By Phillip Francis on 1/27

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#open file for writing
f = open(dir_path + "/testfile.txt", "r")

#read to the file and print to screen
contents = f.read()
print(contents)

#close file

f.close()
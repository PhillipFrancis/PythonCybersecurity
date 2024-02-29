#!/usr/bin/env python3
# Sample script that writes to a file
# By Phillip Francis on 1/27

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#open file for writing
f = open(dir_path + "/testfile.txt", "w")

#write to the file
print("hello world")
    #the \n is a special charecter that essentially moves the command down a line. 
f.write("hello world\n")
f.write("hello world\n")
f.write("hello world\n")

#close file

f.close()
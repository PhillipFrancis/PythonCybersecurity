#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created 

your_name = input('what is your name')
print("Hello {0}".format(your_name))
print(f"hello {your_name}")
print("hello " + your_name)
print("Hello", your_name)
message = "Hello" + " " + your_name
print(message)

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"

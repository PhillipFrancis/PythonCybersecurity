#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created 

first_num = float(input('what is the first number: '))
activity = input('what activity ( + - * / ) ')
second_num = float(input('What is the second number: '))

if activity == "+":
    print(first_num + second_num)
if activity == "-":
    print(first_num - second_num)
if activity == '*':
    print(first_num * second_num)
if activity == '/':
    print(first_num / second_num)


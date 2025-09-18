#!/usr/bin/python3

import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
    raise SystemExit

target = args[0]
user_input = input("What was the parameter? ")

if user_input == target:
    print("Good job!")
else:
    print("Nope, sorry...")
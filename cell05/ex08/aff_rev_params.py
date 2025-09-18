#!/usr/bin/python3

import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for s in reversed(args):
        print(s)

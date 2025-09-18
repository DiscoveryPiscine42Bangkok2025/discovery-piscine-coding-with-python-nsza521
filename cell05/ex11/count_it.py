#!/usr/bin/python3

import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for p in args: 
        print(f"{p}: {len(p)}")
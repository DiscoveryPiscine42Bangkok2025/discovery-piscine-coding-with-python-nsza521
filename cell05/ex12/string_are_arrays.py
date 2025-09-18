#!/usr/bin/python3

import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    s = args[0]
    z = s.count("z") 
    print("z" * z if z > 0 else "none")
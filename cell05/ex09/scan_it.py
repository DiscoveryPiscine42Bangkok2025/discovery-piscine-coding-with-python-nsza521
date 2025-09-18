#!/usr/bin/python3

import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
    raise SystemExit

keyword, text = args

count = text.count(keyword) if keyword else 0

print(count if count > 0 else "none")
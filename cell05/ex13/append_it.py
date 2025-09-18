#!/usr/bin/python3

import sys
import re

args = sys.argv[1:]

if not args:
    print("none")
    raise SystemExit

for word in args:
    if re.search(r'ism\Z', word):
        continue
    print(f"{word}ism")
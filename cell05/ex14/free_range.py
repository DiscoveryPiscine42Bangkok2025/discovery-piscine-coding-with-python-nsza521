#!/usr/bin/python3

import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
    raise SystemExit

try:
    start = int(args[0])
    end = int(args[1])
except ValueError:
    print("none")
    raise SystemExit

step = 1 if start <= end else -1
values = list(range(start, end + step, step))

print(values)
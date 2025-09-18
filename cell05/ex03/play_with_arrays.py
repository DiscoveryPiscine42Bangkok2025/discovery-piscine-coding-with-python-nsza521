#!/usr/bin/env python3

original_array = [-1, 2, 13, 4, 56, 66, 7, 8, 9]

new_array = []
seen = set()

for value in original_array:
    if value > 5 and value not in seen:
        seen.add(value)
        new_array.append(value + 2)
        

print("Original array:", original_array)
print("New array:", new_array)
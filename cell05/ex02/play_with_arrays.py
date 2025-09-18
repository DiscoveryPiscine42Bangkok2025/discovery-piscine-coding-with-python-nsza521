#!/usr/bin/env python3

original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_array = []
for value in original_array:
    if value > 5:
        new_array.append(value + 2)


print("Original array:", original_array)
print("New array:", new_array)
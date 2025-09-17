# advanced_mult.py

# Check if any command-line arguments were passed
import sys
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:  # Outer loop: table number
        print(f"Table de {i}:", end=" ")
        j = 0
        while j <= 10:  # Inner loop: multiplication values
            print(i * j, end=" ")
            j += 1
        print()  # Newline after each table
        i += 1

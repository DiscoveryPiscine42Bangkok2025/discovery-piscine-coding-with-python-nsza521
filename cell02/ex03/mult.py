
num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())

result = num1 * num2

print(f"{num1} x {num2} = {result}")

if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")

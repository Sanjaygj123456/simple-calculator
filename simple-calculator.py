# Simple Calculator for Beginners

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to choose an operation
print("\nChoose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter operation: ")

# Perform calculation based on user's choice
if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operation selected.")

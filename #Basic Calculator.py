#Basic Calculator
def calculator():
    print ("Welcome to the Basic Calculator!")
    print ("Choose an operation: +, -, *, /")

#Get user iput
operation = input ("Enter the operation: ")

if operation not in ['+', '-', '*', '/']:
    print ("Invalid operation. Please try again. ")
    print()

#Get numbers from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter te second number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    print()

# Perform the calculation
if operation == '+':
    result = num1 + num2 
elif operation == '-':
    result = num1 - num2 
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Division by zero is not allowed")
        print()
    result = num1 / num2 

print(f"The result of {num1} {operation} {num2} is: {result}")

# Run the calculator
calculator()

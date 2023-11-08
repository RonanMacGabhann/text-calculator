# Calculator
# This contains the use of dictionaries to hold operations as keys
# and respective values as methods.

# Add
def add(n1, n2):
    return n1 + n2
    
# Subtract
def subtract(n1, n2):
    return n1 - n2
    
# Multiply
def multiply(n1, n2):
    return n1 * n2
    
# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter the first number: "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("Enter the second number: "))

if operation_symbol in operations:
    answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
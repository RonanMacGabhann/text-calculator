# Calculator
# This contains the use of dictionaries to hold operations as keys
# and respective values as methods.
import os
from art import logo

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

# Dictionary Symbols:Methods
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    restart = True
    while restart:
        for key in operations:
            print(key)

        operation_symbol = input("Pick an operation from the line above: ")
        while operation_symbol not in operations:
            print("Invalid operation.")
            operation_symbol = input("Pick a previously stated operation: ")
        
        num2 = float(input("Enter the next number: "))

        answer = round(operations[operation_symbol](num1, num2), 2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_again = input(f"Type 'y' to continue calculating with {answer}, type anything else to start again or type 'n' to exit: ").lower()
        if user_again == "y":
            num1 = answer
        elif user_again =="n":
            restart = False
        else:
            os.system("cls")
            calculator()

print(logo)
calculator()
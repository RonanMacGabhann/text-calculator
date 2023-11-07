from art import logo
print(logo + "\n")
# Art shouldn't clear between runs

# Methods
def addition(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def division(num1, num2):
    result = num1 / num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result

# Description - come back to this!!!!
print("This is a simple text calculator performing an operation on 2 numbers.")
print("----------------------------------------------------------------------\n")

# Storage variables 

def text_calculator():
    first_number = int(input("What's the first number? "))
    operation = input("Enter the operand: '+', '-', '/', '*' ")
    second_number = int(input("What's the second number? "))

    match operation:
        case "+":
            fin_result = addition(first_number, second_number)
        case "-":
            fin_result = subtraction(first_number, second_number)
        case "/":
            fin_result = division(first_number, second_number)
        case "*":
            fin_result = multiplication(first_number, second_number)
        case _:
            print("That's not an operation\n")
            print("Try again!")
            text_calculator()

    print(f"{first_number} {operation} {second_number} = {fin_result}")

text_calculator()
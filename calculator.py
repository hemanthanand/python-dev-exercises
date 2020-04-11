# This code takes the input from the user
# and performs the operation selected by the user

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

class Calculator:
    first_input = float(input('Please enter the first number : '))
    second_input = float(input('Please enter the second number : '))
    operations = ['+', '-', '*', '/']
    print('Here are your operator: '+' '.join(operations))
    operation = input('Please enter the operator : ')
    if operation == '+':
        result = addition(first_input, second_input)
        print('Result : ', result)
    elif operation == '-':
        result = subtraction(first_input, second_input)
        print('Result : ', result)
    elif operation == '*':
        result = multiplication(first_input, second_input)
        print('Result : ', result)
    else:
        result = division(first_input, second_input)
        print('Result : ', result)

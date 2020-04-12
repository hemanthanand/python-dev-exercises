# put your python code here
first = float(input())
second = float(input())
operators = ['+', '-', '/', '*', 'mod', 'pow', 'div']
operation = input()
if operation in operators:
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '*':
        print(first * second)
    elif operation == 'pow':
        print(first ** second)
    elif operation == '/':
        if second == 0:
            print('Division by 0!')
        else:
            print(first / second)
    elif operation == 'mod':
        if second == 0:
            print('Division by 0!')
        else:
            print(first % second)
    else:
        if second == 0:
            print('Division by 0!')
        else:
            print(first // second)

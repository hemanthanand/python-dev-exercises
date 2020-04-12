# put your python code here
user_input = int(input())
if 1900 <= user_input <= 3000:
    if user_input % 4 == 0 and user_input % 100 != 0 or user_input % 400 == 0:
        print('Leap')
    else:
        print('Ordinary')

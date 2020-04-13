user_input = str(input())
# for number in user_input:
#     if number == '0':
#         print('zero')
#     elif number == '1':
#         print('one')
#     elif number == '2':
#         print('two')
#     elif number == '3':
#         print('three')
#     elif number == '4':
#         print('four')
#     elif number == '5':
#         print('five')
#     elif number == '6':
#         print('six')
#     elif number == '7':
#         print('seven')
#     elif number == '8':
#         print('eight')
#     elif number == '9':
#         print('nine')

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for n in user_input:
    print(n)
    print(digits[int(n)])  # printing the nth element of the list 'digits'

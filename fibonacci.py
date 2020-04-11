# This code takes input from the user
# and generates the Fibonacci series

def fibonacci_value(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_value(n-1)+fibonacci_value(n-2)

class Fibonacci:
    series_length = int(input('Hey! Please enter the length of Fibonacci\t'))
    print('You have entered', series_length)
    result = fibonacci_value(series_length)
    print('Fibonacci series: ')
    for i in range(1, series_length+1):
        print(fibonacci_value(i), ' ')

    print('Fibonacci result: ', result)

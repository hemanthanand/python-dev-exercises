number = 1
while number >= 1:
    number = int(input("Enter a number: "))
    if number < 1 or number > 100:
        print ('Please enter only number between 1 to 100')
    else:
        result = number
        while number > 1:
            result *= (number - 1)
            number = number - 1
        print(result)

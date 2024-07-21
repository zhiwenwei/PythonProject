
number = input('Please input an integer number:')

try:
    number = int(number)
    if number % 2 == 0:
        print(number // 2) 
    elif number % 2 ==1:
        print(3 * number + 1)          
except ValueError:
    print("The input is not an integer.")
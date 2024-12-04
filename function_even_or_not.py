# Write a function in Dart called isEven that takes a number as an argument and returns True if the number is even, and False otherwise.

def even_number(number):
    if number %2==0:
        print('The number is not even. So, it is True.')
    else:
        print('The number is not even.So, it is False')
even=int(input('Enter any number :'))

even_number(even)

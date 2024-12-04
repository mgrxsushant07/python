#WAP to print the number btwn (1 to 10) using while loop.

num= int(input("Enter any  number btwn 1-10 :"))

while num < 1 or num > 10:
    print(f'{num} is invalide.')
    num= int(input("Enter any  number btwn 1-10 :"))
print(f'The number is {num}.')



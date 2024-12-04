#WAP to print if the person can vote or not using while loop.

age=int(input('Enter your age :'))
#if age is less than 18 u can't vote
while age <18:
    a= 18-age
    print(f'Your age is less than 18. So,comeback after {a} years. Thankyou...')
    age=int(input('Enter your age :'))
print('You can vote. Thankyou...')


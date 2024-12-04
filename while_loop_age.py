#WAP to print your age.

age = int(input("Enter your age (press q to quit) :"))

while age < 0:
    print('age is negative')
    age=int(input('Enter your age :'))
print(f'You are {age} years old')
    




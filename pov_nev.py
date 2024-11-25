# Write a program to check if a given number is positive, negative, or zero.

number= float(input('Enter any number :'))

# Check conditions

if number >=0:
    print(f"The {number} is positive.")
elif number<=0:
    print(f"The {number} is negative.")
else:
    print(f"The number is zero.")
# Write a program in Dart to calculate power of a certain number. For e.g 5^3=125

def calculate_power(num,power):
    total=num**power
    print(f'The power of {num} is {total}')

num=int(input("Enter the number that u want to power :"))
power=int(input("Enter the power :"))

calculate_power(num,power)

#using maths function
# import math
# def calculate_power(num,power):
#     # Calculate power (number^2)
#      total = math.pow(num, power)
#      print(f"The power of {num} is {total}")


# num=int(input("Enter the number that u want to power :"))
# power=int(input("Enter the power :"))

# calculate_power(num,power)
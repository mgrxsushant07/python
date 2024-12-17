# Write a python program to check if the number is odd or even using try except.

try:
    num= int(input("Enter any number :"))
    if num %2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

except:
    print("Only numbers are allow")
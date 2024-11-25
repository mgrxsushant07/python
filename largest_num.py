#largest number among three number.........
#u can use any of these two prg......

num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
num3 = float(input("Enter the third number :"))

largest = max(num1, num2, num3)
print("The largest number is:", largest)


print() #for gap purpose.....

num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
num3 = float(input("Enter the third number :"))

if num1>num2 and num1>num3 :
    print(f"The {num1} is largest among {num2} and {num3}")
elif num2>num1 and num2>num3 :
    print(f"The {num2} is largest among {num1} and {num2}")
else:
    print(f"The {num3} is largest among {num1} and {num2}")

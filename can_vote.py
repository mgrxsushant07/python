#can vote or can't

age=int(input("Enter your age"))
if age>=18:
    print("You can vote")
else:
    age1=18-age
    print(f"You can't vote. You can vote after {age1} year.")
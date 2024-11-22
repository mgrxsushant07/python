# Suppose, you often go to restaurant with friends and you have to split amount of bill. 
# Write a program to calculate split amount of bill. 
# Formula= (total bill amount) / number of people
# Use User Input

total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))

# Calculating the split amount
split_amount = total_bill / num_people

# Displaying the result
print(f"Each person should pay: {split_amount:.2f}")
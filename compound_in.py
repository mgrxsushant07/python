#To calculate Compound Interest .
#Needed things
#Principle
#Time in years or in months
#Rate of interest
#Number of time interest applied for time period
#Formula to calculate CI


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Compound Interest formula
amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

# Display the result
print(f"The compound interest is {compound_interest:.2f}")
print(f"The total amount after {time} years is {amount:.2f}")
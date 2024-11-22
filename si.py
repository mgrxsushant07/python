#write a program in python that finds simple interest.
#formula to calculate SI = (p *t *r)/100

principal =float(input("Enter principal :"))
time = float(input("Enter time :"))
rate = float(input("Enter rate :"))

calculation = (principal*time*rate//100)

print(f"The calculation of Simple Interest is {calculation}")
# 1. Create an empty list of type string called days. Use the add method to add names of 7 days and print all days.

days =[]

total_days=int(input("Enter how many days :"))

for i in range(1,total_days+1):
     item = input(f"Enter days {i} :")
     days.append(item)
print("\nAll days are: ")

#display item in list
for i in range(0,len(days)):
    print(days[i])
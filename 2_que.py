# 1. Create an empty list of type string called days. Use the add method to add names of 7 days and print all days.
# 2. Add your 7 friend names to the list. Use where to find a name that starts with the alphabet a.
# 3. Write a program that takes a list of numbers and creates a new list containing the squares of all even numbers from the original list.
# 4. Write a program that takes a list of numbers and creates a new list containing the squares of all even numbers from the original list.

names = []
total_names = int(input("Enter how many names : "))

#adding item to list
for i in range(1,total_names+1):
    item = input(f"Enter todo {i}: ")
    names.append(item)
print("\nAll todos are: ")
#display item in list
for i in range(0,len(names)):
    print(names[i])
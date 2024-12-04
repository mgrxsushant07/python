# Get the number of inputs from the user
num_inputs = int(input("How many numbers do you want to cube :"))

print("Enter the numbers:")

# Loop to get numbers and print their cubes
for i in range(num_inputs):
    num = int(input(f"Enter number {i + 1}: "))
    print(f"The cube of {num} is {num ** 3}")

print()#for gap

# Blank todo list
todos = []
total_todo = int(input("Enter how many todo: "))

#adding item to list
for i in range(1,total_todo+1):
    item = input(f"Enter todo {i}: ")
    todos.append(item)
print("\nAll todos are: ")
#display item in list
for i in range(0,len(todos)):
    print(todos[i])
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
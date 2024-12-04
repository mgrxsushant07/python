# # 3. Write a program that takes a list of numbers and creates a new list containing the squares of all even numbers from the original list.

# # number=list(int(input('Enter any numbers :').split()))
# # # for i in range(1,number+1):
# # newlist=[number**2 for number in number]
# # print(newlist)
# # Input: List of numbers
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# # Create a new list with squares of even numbers
# even_squares = [num**2 for num in numbers if num % 2 == 0]

# # Output the new list
# print(f"Squares of even numbers: {even_squares}")
names = ["Alice", "Bob", "Sadikshya", "David"]
for name in names:
    print(name)

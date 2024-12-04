# Write a function in Dart called calculateArea that calculates the area of a rectangle. It should take length and width as arguments, with a default value of 1 for both. Formula: length * width.

def area_of_rectangle(length,width):
    area_of_rectangle=length*width
    print(f'The Area of Rectangle is {area_of_rectangle}.')

#user input
length=int(input("Enter length :"))
width=int(input('Enter width :'))
area_of_rectangle(length,width)
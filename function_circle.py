# Write a program in Dart that find the area of a circle using function. Formula: pi * r * r

def area(pi,r):
    area_of_circle=pi*r**r
    print(f'The Area of circle is {area_of_circle}')
pi=3.14159
r=int(input('Enter radius :')) 
area(pi,r)


#copy from chatgpt
# import math

# def area_of_circle(radius):
#     return math.pi * radius ** 2

# # Example usage
# radius = float(input("Enter the radius of the circle: "))
# area = area_of_circle(radius)
# print(f"The area of the circle is: {area:.2f}")

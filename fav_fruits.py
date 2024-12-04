# 1.Create a tuple of your favorite fruits and display all the fruits.

fav_fruits=('apple','banana','mango','orange','grabs')
for fruit in fav_fruits:
    print(fruit.capitalize())


print() #for gap
# 2.Access and print the first and last fruit in the tuple.

first_fruit=fav_fruits[0]
last_fruit=fav_fruits[4]
print(f"The first fruit in the fruits is {first_fruit}")
print(f"The last fruit in the fruits is {last_fruit}")

# 3.Attempt to change the second fruit in the tuple and observe what happens (this should raise an error since tuples are unchangeable).
# fav_fruits[1]='Watermelon'
# print(fruit)

#if u try to change the fruits name u will see the error liike below :
# Traceback (most recent call last):
#   File "c:\Users\Asus\Desktop\pyton learing\fav_fruits.py", line 15, in <module>
#     fav_fruits[1]='Watermelon'
#     ~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment   
print() #for gap

# 4.Combine this tuple with another tuple of your favorite vegetables, and print the resulting combined tuple.
fav_vegetable=('Carrot', 'Spinach', 'Broccoli', 'Tomato', 'Cauliflower')

#combining the fav_fruts and fav_vegetables
fav_combination=fav_fruits+fav_vegetable
print("Favorite Fruits and Vegetables:")
print(", ".join(fav_combination))

print() # for gap
# 5.Find and print the length of the combined tuple using the len() function.
combine_number=len(fav_combination)
print(f"The length of combined fav veg and fav fru is :{combine_number}")



### Create Class Called Customer with properties name, age
### Create display Method that display all details.
### Create 3 objects of Customer and display all details.
# Write a dart program to create a class Laptop with properties [id, name, ram] and create 3 objects of it and print all details.
# Write a dart program to create a class House with properties [id, name, price]. Create a constructor of it and create 3 objects of it. Add them to the list and print all details.


class customer:
    def __init__(self,name,age,address):
        self.name = name
        self.age=age
        self.address=address
       
      

    def display(self):
        print(f'Your name is {self.name} age is {self.age} and address is {self.address}' )

#object creation

p1=customer(name="Sushant",age=17,address="Butwal")
p2=customer(name='Aryan',age=17,address="")
p3=customer(name='Shudik',age=17)

p1.display()
p2.display()
p3.display()
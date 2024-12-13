class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age=age
        self.gender=gender
      

    def display(self):
        print(f'Your name is {self.name} age is {self.age} and gender is {self.gender}')

#object creation

p1=person(name="Sushant",age=17,gender="male")
p2=person(name='Aryan',age=17, gender="male")
p3=person(name='Shudik',age=17, gender="male")

p1.display()
p2.display()
p3.display()   
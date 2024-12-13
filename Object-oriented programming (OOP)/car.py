#encapslutation

class car:
    def __init__(self,id,name,brand):
        self.id=id
        self.__name=name
        self.brand=brand
#for dispaly name only using getter
    def get_name(self):
        return self.__name
    
#to display
    def display_details(self):
        print(f"Car id is {self.id}. Car name is {self.__name} and it's brand is {self.brand}.")

c1=car(57,"Mustang", "Ford")
c2=car("07","Ferrari 488", "Ferrari")

# to call
c1.display_details()
c2.display_details()
#Call usiing encapsulation method
print(c1.get_name())
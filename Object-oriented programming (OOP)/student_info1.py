#to display student name, address, phone using function/OOP/encapsulation


class student:
    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.__phone=phone

    def set_phone(self,phone):
        self.__phone=phone

    def display_detail(self):
        print(f"Student name is {self.name}. {self.name} is from {self.address} and phone nummber is {self.__phone}")

s=student("","","")
s.name=input('Enter student name :')
phone=input('Enter student phone number :')
s.set_phone(phone)
s.address=input('Enter student address :')

s.display_detail()
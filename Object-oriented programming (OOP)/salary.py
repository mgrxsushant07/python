#Bank name, bank employee, age, address, salary

class Bank:
    def __init__(self, employee_name, address, contact, salary):
        self.employee_name = employee_name
        self.address = address
        self.contact = contact
        self.__salary = salary  # Private attribute

    def set_salary(self, salary):
        self.__salary = salary  # Method to set salary

    def display_detail(self):
        print(f'The name of the bank employee is {self.employee_name}. Address is {self.address}. Contact is {self.contact}, and his/her total salary is {self.__salary}')

# Object creation
em = Bank("", "", "", 0)    

# Taking input from the user
em.employee_name = input("Enter employee name: ")
em.address = input("Enter employee address: ")
em.contact = input("Enter employee contact: ")
salary = input("Enter the total salary of employee: ")

# Setting the salary using the method
em.set_salary(salary)

# Display the details
em.display_detail()

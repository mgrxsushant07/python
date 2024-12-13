class Customer:
    def __init__(self, name, email, phone, balance):
        self.name = name
        self.email = email
        self.phone = phone
        self.balance = balance
 
    def deposit(self, amount):
        if amount<=0:
            return
        self.balance += amount
 
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
 
    def check_balance(self):
        print(f"{self.name} balance is {self.balance}")
 
c1 = Customer("Sumit", "sumit@gmail.com", "837237", 4000)
c2 = Customer("Adatya","adatya@gmail.com","232323", 2500 )
c3 = Customer("Dipen", "dipen@gmail.com", "232323", 3500)
 
c1.deposit(500)
c1.withdraw(700)
c1.withdraw(200)
 
c2.deposit(250)
 
c3.withdraw(100)
 
c1.check_balance() # 3600
c2.check_balance() # 2750
c3.check_balance() #3400  
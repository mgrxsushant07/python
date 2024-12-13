class customer:
    def __init__(self, name, account_no, balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance

    def deposit(self,amount):
        if amount <=0:
            print('Invalid amount')
            return
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance >=amount:
            self.balance -=amount
        else:
            print("You have not enough money to withdraw")
    
    def check_balance(self,amount):
        print(f"{self.name} balance is {self.balance}") 

c1=customer('Aryan',507,57500)
c2=customer('Aayush',512,70820)


c1.deposit(5000)
c1.withdraw(7075)

c2.deposit(500)
c2.withdraw(10000)

c1.check_balance()
c2.check_balance()

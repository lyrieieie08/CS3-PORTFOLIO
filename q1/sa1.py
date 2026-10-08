class Account:
    name=""
    number=""
    __balance=0
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def getBalance(self):
        return self.__balance
    def deposit(self,amount):
        self.balance-=amount
    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
    def 

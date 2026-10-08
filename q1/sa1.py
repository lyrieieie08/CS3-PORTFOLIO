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
    def __str__(self):
        return self.name + "[" + self.number + "] P " + str(self.__balance)
    def __del__(self):
        print("Account", self.number, "closed")

class SavingsAccount(Account):
    __interest = 0.05
    def addInterest(self):
        #super().__balance += super().__balance()*self.__interest
        interestToAdd = super().getBalance() * self.__interest

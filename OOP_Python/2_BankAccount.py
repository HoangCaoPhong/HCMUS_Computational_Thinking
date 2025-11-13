class BankAccount:
    def __init__(self, accNum, owner, balance = 0):
        self.__accNum = accNum
        self.__owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Your balance: +{amount} USD")
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Your balance: -{amount} USD")
        else:
            print(f"Your account don't have enough money to withdraw {amount} USD")

    def getBalance(self):
        return self.__balance
    

acc1 = BankAccount(000, "Phong", 100)    
print(f"Your account have ${acc1.getBalance()} ")
acc1.deposit(100)
print(f"Your account have ${acc1.getBalance()} ")
acc1.withdraw(300)
print(f"Your account have ${acc1.getBalance()} ")
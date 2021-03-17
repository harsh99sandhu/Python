class Account:
    def __init__(self, initial_amount):
        self.__balance = initial_amount
    def withdraw(self,amount):
        self.__balance = self.__balance - amount
        print(self.__balance) #stmt3
    def deposit(self,amount):
        self.__balance = self.__balance + amount


ac = Account(1000)
ac.deposit(2000) #stmt1
ac.withdraw(1000) #stmt2

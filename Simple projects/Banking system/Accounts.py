from datetime import datetime
from abc import ABC,abstractmethod

class Account:
    def __init__(self,account_number,balance=0) -> None:
        self.account_number = account_number
        self.balance = balance
        self.transcation = []
    
    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self,value):
        self.__account_number = value
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,value):
        self.__balance = value
    
    @abstractmethod
    def deposit(self,amount):
        self.balance += amount
        self.transcation.append((str(datetime.now()),"Deposit",amount))
        return self.balance
    
    @abstractmethod
    def withdraw(self,amount):
        if self.balance < amount:
            raise ValueError("You have not enough money")
        self.balance -= amount
        self.transcation.append((datetime.now(),"Withdraw",amount))
        return self.balance
        
class SavingsAccount(Account):
    def deposit(self,amount):
        super().deposit(amount)

    def withdraw(self,amount):
        super().withdraw(amount)

class CheckingAccount(Account):
    def deposit(self,amount):
        super().deposit(amount)

    def withdraw(self,amount):
        super().withdraw(amount)

    
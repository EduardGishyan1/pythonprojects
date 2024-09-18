from account import *

class SavingAccounts(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, interest_rate: float) -> None:
        super().__init__(account_number, balance, account_type)
        self.setInterestRate(interest_rate)
        self.__current_balance = self.getBalance()
    
    def deposit(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0:
            interest = self.__interest_rate * amount / 100
            self.__current_balance += interest
            self.setBalance(self.__current_balance)
        else:
            raise ValueError("Enter valid amount")
    
    def withdraw(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0:
            interest = self.__interest_rate * amount / 100
            if self.__current_balance >= amount + interest:
                self.__current_balance -= amount + interest
                self.setBalance(self.__current_balance)
            else:
                raise ValueError("You have not enough money")
        else:
            raise ValueError("Enter valid amount")
        
    def transfer(self, destination: Account, amount: float) -> None:
        if isinstance(amount,float) and amount >= 0:
            interest = self.__interest_rate * amount / 100
            if self.__current_balance > amount + interest:
                interest = amount * self.__interest_rate / 100
                self.__current_balance -= amount + interest
                self.setBalance(self.__current_balance)
                destination.deposit(amount)
            else:
                raise ValueError("You haven't enough money")
        else:
            raise ValueError("Enter valid amount")
    
    def show_balance(self) -> float:
        return self.__current_balance


    def setInterestRate(self,interest_rate):
        if isinstance(interest_rate,float) and interest_rate > 0:
            self.__interest_rate = interest_rate
        else:
            raise ValueError("Enter valid value")
    
    def getInterestRate(self):
        return self.__interest_rate
    
    def setAccountType(self, account_type):
        if isinstance(account_type,str):
            self.__account_type = account_type
    
    def get_account_type(self) -> str:
        return self.__account_type
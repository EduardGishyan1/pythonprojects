from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,account_number:int,balance:float,account_type:str) -> None:
        self.setAccountNumber(account_number)
        self.setBalance(balance)
        self.setAccountType(account_type)
    @abstractmethod
    def deposit(self,amount:float) -> None:
        ...
    @abstractmethod
    def withdraw(self,amount:float) -> None:
        ...
    @abstractmethod
    def transfer(self,destination:'Account',amount:float) -> None:
        ...
    @abstractmethod
    def show_balance(self) -> None:
        ...
    @abstractmethod
    def get_account_type(self) -> str:
        ...
    def setAccountNumber(self,account_number):
        if isinstance(account_number,int) and account_number > 0:
            self.__account_number = account_number
        else:
            raise ValueError("Enter valid value")

    def setBalance(self,balance):
        if isinstance(balance,float) and balance > 0:
            self.__balance = balance
        else:
            raise ValueError("Enter valid value")
    
    def setAccountType(self,account_type):
        if isinstance(account_type,str) and account_type:
            self.__account_type = account_type
        else:
            raise ValueError("Enter valid value")

    def getAccountNumber(self):
        return self.__account_number
    
    def getBalance(self):
        return self.__balance
    
    def getAccountType(self):
        return self.__account_type
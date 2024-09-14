from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,account_number:int,balance:float,account_type:str) -> None:
        self.set_acc_Number(account_number)
        self._account_number = account_number
        self.set_balance(balance)
        self._balance = balance
        self._account_type = account_type
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

    def set_acc_Number(self,number):
        if isinstance(number,int) and number > 0:
            self._account_number = number
        else:
            raise ValueError("Enter number")
        
    def set_balance(self,balance):
        if isinstance(balance,float) or isinstance(balance,int):
            self._balance = balance
        else:
            raise ValueError("Enter number")
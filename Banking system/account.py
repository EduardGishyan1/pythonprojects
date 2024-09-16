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

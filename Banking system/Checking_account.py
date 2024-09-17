from account import *

class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str,overdraft_limit:float) -> None:
        super().__init__(account_number, balance, account_type)
        self._overdraft_limit = overdraft_limit
        
    def deposit(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0:
            self._balance += amount
        else:
            raise ValueError("Enter valid amount")
    
    def withdraw(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0 and self._overdraft_limit >= amount:
            if self._balance >= amount:
                self._balance -= amount
            else:
                raise ValueError("You have not enough money")
        else:
            raise ValueError("Enter valid amount")
        
    def transfer(self, destination: Account, amount: float) -> None:
        if isinstance(amount,float) and amount >= 0 and self._overdraft_limit >= amount:
            if self._balance > amount:
                self._balance -= amount
                destination.deposit(amount)
            else:
                raise ValueError("You haven't enough money")
        else:
            raise ValueError("Enter valid amount")
    
    def show_balance(self) -> float:
        return self._balance

    def get_account_type(self) -> str:
        return self._account_type

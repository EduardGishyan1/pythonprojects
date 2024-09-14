from account import *

class SavingAccounts(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, interest_rate: float) -> None:
        super().__init__(account_number, balance, account_type)
        self._interest_rate = interest_rate
    
    def deposit(self,amount:float) -> None:
        if amount >= 0 and isinstance(amount,float) or isinstance(amount,int):
            interest = self._interest_rate * amount / 100
            self._balance += amount - interest
        else:
            raise ValueError("Enter valid amount")
    
    def withdraw(self,amount:float) -> None:
        if amount >= 0 and isinstance(amount,(float,int)):
            interest = self._interest_rate * amount / 100
            if self._balance >= amount + interest:
                self._balance -= amount + interest
            else:
                raise ValueError("You have not enough money")
        else:
            raise ValueError("Enter valid amount")
        
    def transfer(self, destination: Account, amount: float) -> None:
        if isinstance(amount,(float,int)) and amount >= 0:
            interest = self._interest_rate * amount / 100
            if self._balance > amount + interest:
                interest = amount * self._interest_rate / 100
                self._balance -= amount + interest
                destination.deposit(amount)
            else:
                raise ValueError("You haven't enough money")
        else:
            raise ValueError("Enter valid amount")
    
    def show_balance(self) -> float:
        return self._balance

    def get_account_type(self) -> str:
        return self._account_type

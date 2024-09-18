from account import *

class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str,overdraft_limit:float) -> None:
        super().__init__(account_number, balance, account_type)
        self.setOverdraftLimit(overdraft_limit)
        self.__current_balance = self.getBalance()
        
    def deposit(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0:
            self.__current_balance += amount
        else:
            raise ValueError("Enter valid amount")
    
    def withdraw(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0 and self._overdraft_limit >= amount:
            if self.__current_balance >= amount:
                self.__current_balance -= amount
                self.setBalance(self.__current_balance)
            else:
                raise ValueError("You have not enough money")
        else:
            raise ValueError("Enter valid amount")
        
    def transfer(self, destination: Account, amount: float) -> None:
        if isinstance(amount,float) and amount >= 0 and self.__overdraft_limit >= amount:
            if self.__current_balance > amount:
                self.__current_balance -= amount
                destination.deposit(amount)
            else:
                raise ValueError("You haven't enough money")
        else:
            raise ValueError("Enter valid amount")
    
    def show_balance(self) -> float:
        return self.__current_balance

    def get_account_type(self) -> str:
        return self.__account_type
    
    def setOverdraftLimit(self,overdraft_limit):
        if isinstance(overdraft_limit,float) and overdraft_limit > 0:
            self.__overdraft_limit = overdraft_limit
        else:
            raise ValueError("Enter valid value")

    def getOverdraftLimit(self):
        return self.__overdraft_limit

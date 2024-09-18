from account import *
from typing import List

class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str,joint_owners: List[str]) -> None:
        super().__init__(account_number, balance, account_type)
        self.setJointOwners(joint_owners)
        self.__current_balance = self.getBalance()
    
    def deposit(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0:
            self.__current_balance += amount
            self.setBalance(self.__current_balance)
        else:
            raise ValueError("Enter valid amount")
    
    def withdraw(self,amount:float) -> None:
        if isinstance(amount,float) and amount >= 0:
            if self.__current_balance >= amount:
                self.__current_balance -= amount
                self.setBalance(self.__current_balance)
            else:
                raise ValueError("You have not enough money")
        else:
            raise ValueError("Enter valid amount")
        
    def transfer(self, destination: Account, amount: float) -> None:
        if isinstance(amount,float) and amount >= 0:
            if self.__current_balance > amount:
                self.__current_balance -= amount
                self.setBalance(self.__current_balance)
                destination.deposit(amount)
            else:
                raise ValueError("You haven't enough money")
        else:
            raise ValueError("Enter valid amount")
    
    def show_balance(self) -> float:
        return self.__current_balance

    def get_account_type(self) -> str:
        return self.__account_type
    
    def add_owner(self,customer:str):
        self._joint_owners.append(customer)

    def setJointOwners(self,joint_owners):
        if isinstance(joint_owners,list):
            self.__joint_owners = joint_owners
        else:
            raise ValueError("Enter valid value")
    
    def getJointOwners(self):
        return self.__joint_owners

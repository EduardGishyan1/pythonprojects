from account import Account
from typing import List

class Customer:
    def __init__(self,name:str,contact_info:str,accounts:List[Account]) -> None:
        self._name = name
        self._contact_info = contact_info
        self._accounts = accounts
        self._transcation_history = []

    def add_account(self,account:Account) -> None:
        if not account in self._transcation_history:
            self._accounts.append(account)
            self._transcation_history.append(account)
        else:
            print("You have it...")
    
    def view_accounts(self) -> None:
        for account in self._accounts:
            print(f"account is {type(account).__name__}")

    def view_transcation_history(self):
        for history in self._transcation_history:
            print(f"Added account {type(history).__name__}")
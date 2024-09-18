from account import Account
from typing import List

class Customer:
    def __init__(self,name:str,contact_info:str,accounts:List[Account]) -> None:
        self.setName(name)
        self.setContactInfo(contact_info)
        self.setAccounts(accounts)
        self.__transcation_history = []

    def add_account(self,account:Account) -> None:
        if not account in self.__accounts:
            self.__accounts.append(account)
            self.__transcation_history.append(account)
        else:
            print("You have it...")
    
    def view_accounts(self) -> None:
        for account in self.__accounts:
            print(f"account is {type(account).__name__}")

    def view_transcation_history(self):
        for history in self.__transcation_history:
            print(f"Added account {type(history).__name__}")
    
    def setName(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            raise ValueError("Enter valid value")

    def setContactInfo(self,contact_info):
        if isinstance(contact_info,str):
            self.__contact_info = contact_info
        else:
            raise ValueError("Enter valid value")

    def setAccounts(self,accounts):
        if isinstance(accounts,list):
            self.__accounts = accounts
        else:
            raise ValueError("Enter valid value")

    def getName(self):
        return self.__name
    
    def getContactInfo(self):
        return self.__contact_info
    
    def getAccounts(self):
        return self.__accounts

class Customer:
    def __init__(self,name,contact_information) -> None:
        self.name = name
        self.contact_information = contact_information
        self.accounts = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def contact_information(self):
        return self.__contact_information
    
    @contact_information.setter
    def contact_information(self,value):
        self.__contact_information = value

    def add_account(self,account):
        self.accounts.append(account)
    
    def view_accounts(self):
        if self.accounts:
            return [(type(account).__name__,account.balance) for account in self.accounts]
        return []
    
    def transfer_funds(self,from_account,to_account,amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)

from datetime import datetime

class Transcation:
    def __init__(self,debited,credited,amount,transcation_type) -> None:
        self.debited = debited
        self.credited = credited
        self.amount = amount
        self.transcation_type = transcation_type
        self.datetime = datetime.now()


    def __str__(self) -> str:
        return f"Datetime {str(self.datetime)} , Transcation type: {self.transcation_type}, credited: {self.credited}, debited: {self.debited}, amount: {self.amount}"
    
    @property
    def debited(self):
        return self.__debited
    
    @debited.setter
    def debited(self,value):
        self.__debited = value
    
    @property
    def credited(self):
        return self.__credited

    @credited.setter
    def credited(self,value):
        self.__credited = value

    @property 
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,value):
        self.__amount = value
    
    @property
    def transcation_type(self):
        return self.__transcation_type
    
    @transcation_type.setter
    def transcation_type(self,value):
        self.__transcation_type = value



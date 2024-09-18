from typing import List,Optional
import datetime

class Transcation:
    def __init__(self,from_account:type,to_account:Optional[type],amount:float,transcation_type:str,timestamp:datetime.datetime) -> None:
        self.setFromAccount(from_account)
        self.setToAccount(to_account)
        self.setAmount(amount)
        self.setTranscationType(transcation_type)
        self.setTimeStamp(timestamp)

    def log(self):
        print(f"from {type(self._from_account).__name__} account")
        print(f"to {type(self._to_account).__name__} account")
        print(f"amount is {self._amount}")
        print(f"Transcation type is {self._transcation_type}")
        print(f"Timestamp is {self._timestamp}")
    
    def setFromAccount(self,from_account):
        if isinstance(from_account,type):
            self._from_account = from_account
        else:
            raise ValueError("Enter valid value")
    
    def setToAccount(self,to_account):
        if isinstance(to_account,type):
            self._to_account = to_account
        else:
            raise ValueError("Enter valid value")
    
    def setAmount(self,amount):
        if isinstance(amount,float):
            self._amount = amount
        else:
            raise ValueError("Enter valid value")
    
    def setTranscationType(self,transcation_type):
        if isinstance(transcation_type,str):
            self._transcation_type = transcation_type
        else:
            raise ValueError("Enter valid value")
        
    def setTimeStamp(self,timestamp):
        if timestamp:
            self._timestamp = timestamp

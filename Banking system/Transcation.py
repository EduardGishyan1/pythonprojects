from typing import List,Optional
import datetime

class Transcation:
    def __init__(self,from_Account:type,to_account:Optional[type],amount:float,transcation_type:str,timestamp:datetime.datetime) -> None:
        self._from_Account = from_Account
        self._to_account = to_account
        self._amount = amount
        self._transcation_types = transcation_type
        self._timestamp = timestamp

    def log(self):
        print(f"from {type(self._from_Account).__name__} account")
        print(f"to {type(self._to_account).__name__} account")
        print(f"amount is {self._amount}")
        print(f"Transcation type is {self._transcation_types}")
        print(f"Timestamp is {self._timestamp}")
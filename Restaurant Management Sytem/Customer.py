from typing import Any
from Order import Order
class Customer:
    __slots__ = ("name","__contact_info","order_history")
    def __init__(self,name:str,contact_info:Any) -> None:
        self.name = name
        self.__contact_info = contact_info
        self.order_history : list = []
    
    def place_order(self,order:Order):
        self.order_history.append(order)
    
    def view_order_history(self):
       return self.order_history
    

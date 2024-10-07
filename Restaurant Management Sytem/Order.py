from abc import abstractmethod
from Customer import Customer
from MenuItem import MenuItem
class Order:
    
    __slots__ = ("customer","menu_items","total_price")
    def __init__(self,customer:Customer) -> None:
        self.customer = customer
        self.menu_items:list = []
    
    @abstractmethod
    def add_menu_item(self,menu_item:MenuItem):
        self.menu_items.append(menu_item)
        self.calculate_total_price()
    
    @abstractmethod
    def calculate_total_price(self):
        return sum(item.price for item in self.menu_items)

class DineInOrder(Order):
    __slots__ :tuple = tuple()
    def add_menu_item(self, menu_item:MenuItem):
        super().add_menu_item(menu_item)
    
    def calculate_total_price(self):
        return super().calculate_total_price()

class TakeAwayOrder(Order):
    __slots__ :tuple = tuple()
    def add_menu_item(self, menu_item:MenuItem):
        super().add_menu_item(menu_item)
    
    def calculate_total_price(self):
        return super().calculate_total_price()

class DeliveryOrder(Order):
    __slots__ : tuple = tuple()
    def add_menu_item(self, menu_item:MenuItem):
        super().add_menu_item(menu_item)
    
    def calculate_total_price(self):
        return super().calculate_total_price()


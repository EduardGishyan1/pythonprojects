from typing import List

class MenuItem:
    __slots__ = ("name","price","ingredients")
    def __init__(self,name:str,price:float,ingredients:List[str]) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients

class Appetizer(MenuItem):
    __slots__ = ("serving_size",)
    def __init__(self,name:str,price:float,ingredients:List[str],serving_size:int) -> None:
        super().__init__(name,price,ingredients)
        self.serving_size = serving_size

class Entree(MenuItem):
    __slots__ = ("cooking_method","spiciness")
    def __init__(self,name:str,price:float,ingredients:List[str],cooking_method:str,spiciness:str) -> None:
        super().__init__(name, price, ingredients)
        self.cooking_method = cooking_method
        self.spiciness = spiciness

class Dessert(MenuItem):
    __slots__ = ("calories",)
    def __init__(self,name:str,price:float,ingredients:List[str],calories:int) -> None:
        super().__init__(name, price, ingredients)
        self.calories = calories

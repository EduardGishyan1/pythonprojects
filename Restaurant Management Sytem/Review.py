from Order import Order
class Review:
    __slots__ = ("customer_name","order","rating","comments")
    def __init__(self,customer_name:str,order:object,rating:int,comments:str) -> None:
        self.customer_name = customer_name
        self.setOrder(order)
        self.setRating(rating)
        self.comments = comments
    
    def setOrder(self,order:Order):
        if order:
            self.order = order
        else:
            raise TypeError("Enter valid order")
    
    def setRating(self,rating:int):
        if isinstance(rating,int) and 0 <= rating <= 5:
            self.rating = rating
        else:
            raise TypeError("higher or equal 0 and less than 5")

    
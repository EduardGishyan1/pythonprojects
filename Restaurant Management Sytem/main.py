from MenuItem import *
from Order import *
from Customer import Customer
from Review import Review

if __name__ == "__main__":
    appetizer = Appetizer("Spring Rolls", 5.99, ["rice paper", "vegetables"],2)
    entree = Entree("Spicy Curry", 12.99, ["chicken", "spices"],"grill", spiciness="hot")
    dessert = Dessert("Chocolate Cake", 4.99, ["chocolate", "flour"], calories=350)

    customer = Customer("Ann", "ann@example.com")

    order = DineInOrder(customer)
    order.add_menu_item(appetizer)
    order.add_menu_item(entree)
    
    customer.view_order_history()
    print(f"Total Price: {order.calculate_total_price()}")

    review = Review(customer.name, order, rating=5, comments="Delicious food!")
    print(f"Name: {review.customer_name} - Review: {review.comments} - Rating: {review.rating}/5")
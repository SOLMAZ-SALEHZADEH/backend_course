from models.product import Product

class CartItem:
    """Represent an item in the cart with a product and its quantity."""
    def __init__(self, product_obj: Product, quantity: int):
        self.quantity = quantity
        self.product_obj = product_obj
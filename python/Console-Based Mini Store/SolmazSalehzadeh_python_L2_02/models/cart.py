from models.cartitem import CartItem
from store import Store

class Cart:
    """Represent the whole basket with all products and their quantities."""
    def __init__(self, store: Store) -> None:
        self.items: list[CartItem] = []
        self.store = store

    def find_cart_item(self, name: str) -> CartItem | None:
        for item in self.items:
            if item.product_obj.name == name:
                return item
        return None

    def total_price(self) -> float:
        """Calculate the total price of the cart."""
        cost = 0
        for item in self.items:
            cost += item.product_obj.price * item.quantity
        return cost

    def add_to_cart(self, product_name: str, quantity: int) -> None:
        """Add a product to the cart."""
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        product_obj = self.store.find_product(product_name)

        if not product_obj:
            raise ValueError('The selected product has not been found')

        if product_obj.stock < quantity:
            raise ValueError("Not enough stock")

        cart_item = self.find_cart_item(product_name)

        if cart_item:
            cart_item.quantity += quantity
        else:
            self.items.append(CartItem(product_obj, quantity))

        product_obj.stock -= quantity

    def remove_from_cart(self, product_name: str) -> None:
        """Remove a product completely from the cart."""
        cart_item = self.find_cart_item(product_name)

        if not cart_item:
            raise ValueError('"Product is not in cart"')

        product_obj = self.store.find_product(product_name)

        if not product_obj:
            raise ValueError('The selected product has not been found')

        product_obj.stock += cart_item.quantity
        self.items.remove(cart_item)

    def view_cart(self) -> list[CartItem]:
        """Return the items in the cart."""
        return self.items

    def checkout(self) -> tuple[list[CartItem], float]:
        
        """Complete checkout and return purchased items and total price."""
        if not self.items:
            raise ValueError('the basket is empty')
        
        items = self.items.copy()
        total_price = self.total_price()
        self.items = []
        return (items,total_price)

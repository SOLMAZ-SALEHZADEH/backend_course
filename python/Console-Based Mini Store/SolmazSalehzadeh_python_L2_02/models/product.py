class Product:
    """Represent a product available in the store."""
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
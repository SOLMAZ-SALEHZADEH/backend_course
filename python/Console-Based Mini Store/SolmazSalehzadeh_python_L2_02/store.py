from  models.product import Product
class Store:
    """Represent a store responsible for managing store products."""
    def __init__(self) -> None:
        self.products: list[Product] = []

    def list_products(self) -> list[str]:
        return [
            f'[{index}] {product.name} - ${product.price} (stock:{product.stock})'
            for index, product in enumerate(self.products, start=1)
        ]

    def find_product(self, product_name: str) -> Product | None:
        """Find a product by name."""
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def add_product(self, name: str, price: float, stock: int) -> None:
        product = Product(name, price, stock)
        self.products.append(product)


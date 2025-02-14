class Product:
    """Represents a product with details like name, price, and stock."""

    def __init__(self, product_id: int, name: str, price: float, category: str, quantity_in_stock: int):
        """Initialize product with ID, name, price, category, and stock quantity."""
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def __str__(self):
        """Return product details as a formatted string."""
        return f"Product[ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Category: {self.category}, Stock: {self.quantity_in_stock}]"

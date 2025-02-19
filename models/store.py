class Store:
    """Represents a store with products and location."""

    #Store Act as a container of all products
    def __init__(self, store_id: int, name: str, location: str, product_list: list):
        """Initialize store with ID, name, location, and products."""
        self.store_id = store_id
        self.name = name
        self.location = location
        self.product_list = {product.product_id: product for product in product_list}  # Store products as a dictionary

    def __str__(self):
        """Return store details as a formatted string."""
        return f"Store[ID: {self.store_id}, Name: {self.name}, Location: {self.location}, Products: {len(self.product_list)}]"

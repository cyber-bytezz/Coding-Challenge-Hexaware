class Cart:
    """Represents a customer's shopping cart."""

    def __init__(self, cart_id: int, customer_id: int):
        """Initialize cart with ID and customer association."""
        self.cart_id = cart_id
        self.customer_id = customer_id
        self.dict_product_quantity = {}  # Stores {product_id: quantity}

    def add_product(self, product_id: int, quantity: int):
        """Add product or update quantity if already in cart."""
        self.dict_product_quantity[product_id] = self.dict_product_quantity.get(product_id, 0) + quantity

    def remove_product(self, product_id: int, quantity: int):
        """Remove or reduce product quantity; delete if zero."""
        if product_id in self.dict_product_quantity:
            self.dict_product_quantity[product_id] -= quantity
            if self.dict_product_quantity[product_id] <= 0:
                del self.dict_product_quantity[product_id]

    def get_cart_items(self):
        """Return cart contents as a dictionary."""
        return self.dict_product_quantity

    def __str__(self):
        """Return cart details as a formatted string."""
        return f"Cart[ID: {self.cart_id}, CustomerID: {self.customer_id}, Products: {self.dict_product_quantity}]"

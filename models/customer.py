class Customer:
    """Represents a customer with basic details."""

    def __init__(self, customer_id: int, name: str, email: str):
        """Initialize customer with ID, name, and email."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        """Return customer details as a formatted string."""
        return f"Customer[ID: {self.customer_id}, Name: {self.name}, Email: {self.email}]"

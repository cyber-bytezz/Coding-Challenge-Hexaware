from abc import ABC, abstractmethod

class StoreServices(ABC):
    """Abstract class defining store service operations."""

    @abstractmethod
    def search_product_by_name(self, name: str):
        """Search for a product by name."""
        pass

    @abstractmethod
    def search_product_by_category(self, category: str):
        """Search for products by category."""
        pass

    @abstractmethod
    def add_product_to_cart(self, cart, product_id, quantity):
        """Add a product to the cart."""
        pass

    @abstractmethod
    def remove_product_from_cart(self, cart, product_id, quantity):
        """Remove a product from the cart."""
        pass

    @abstractmethod
    def purchase(self, cart, customer):
        """Process the cart purchase and generate a bill."""
        pass

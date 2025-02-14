from services.store_services import StoreServices
from exceptions.item_out_of_stock import ItemOutOfStock
from datetime import datetime


class StoreServiceImpl(StoreServices):
    """Implements store services for product management and transactions."""

    def __init__(self, store):
        """Initialize store service with a store instance."""
        self.store = store

    def search_product_by_name(self, name: str):
        """Return products matching the name."""
        return [product for product in self.store.product_list.values() if name.lower() in product.name.lower()]

    def search_product_by_category(self, category: str):
        """Return products matching the category."""
        return [product for product in self.store.product_list.values() if category.lower() == product.category.lower()]

    def check_reorder_levels(self, product_id):
        """Reorder stock if product quantity falls below 5."""
        product = self.store.product_list.get(product_id)
        if product and product.quantity_in_stock < 5:
            product.quantity_in_stock += 50
            print(f"Stock for '{product.name}' was low. Ordered 50 more units. New stock: {product.quantity_in_stock}")

    def add_product_to_cart(self, cart, product_id, quantity):
        """Add product to cart if stock is available; else raise an exception."""
        product = self.store.product_list.get(product_id)
        if product:
            if product.quantity_in_stock >= quantity:
                cart.add_product(product_id, quantity)
                product.quantity_in_stock -= quantity
                print(f"{quantity} x {product.name} added to cart.")
                self.check_reorder_levels(product_id)
            else:
                raise ItemOutOfStock(f"{product.name} is out of stock!")
        else:
            print("Product not found!")

    def remove_product_from_cart(self, cart, product_id, quantity):
        """Remove product from cart or reduce its quantity."""
        cart.remove_product(product_id, quantity)
        print(f"{quantity} units removed from cart.")

    def purchase(self, cart, customer):
        print(f"\nBill for {customer.name} ({customer.email})")
        print(f"Store: {self.store.name} - Location: {self.store.location}")
        print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        total = 0
        for product_id, quantity in cart.dict_product_quantity.items():
            product = self.store.product_list.get(product_id)
            item_total = product.price * quantity
            total += item_total
            print(f"{product.name} x {quantity} = ₹{item_total}")

        print("Total Bill Amount:", total)
        cart.dict_product_quantity.clear()
        print(" Purchase successful! Thank you for shopping with us.")



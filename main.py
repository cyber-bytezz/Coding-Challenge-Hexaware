from models.customer import Customer
from models.product import Product
from models.store import Store
from models.cart import Cart
from services.store_service_impl import StoreServiceImpl
from exceptions.item_out_of_stock import ItemOutOfStock

# Initialize sample products
products = [
    Product(1, "Laptop", 50000, "Electronics", 10),
    Product(2, "Phone", 20000, "Electronics", 5),
    Product(3, "Shoes", 2000, "Fashion", 15),
]

# Create store and services
store = Store(1, "TechStore", "TamilNadu", products)
store_service = StoreServiceImpl(store)

# Get customer details dynamically at the start
print(f"\nWelcome to {store.name} - Location: {store.location}")

name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip()

# Validate customer details
while not name or not email:
    print("Name and Email are required!")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()

# Create customer object dynamically
customer = Customer(1, name, email)
cart = Cart(1, customer.customer_id)

# Menu-driven user interface
while True:
    print("\nSelect an option:")
    print("1. Search Product by Name")
    print("2. Search Product by Category")
    print("3. Add Product to Cart")
    print("4. Remove Product from Cart")
    print("5. Purchase")
    print("6. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter product name: ").strip()
        results = store_service.search_product_by_name(name)
        print("\n".join(str(prod) for prod in results) if results else "No products found.")

    elif choice == "2":
        # Extract unique categories from product list
        unique_categories = set(product.category for product in store.product_list.values())

        # Display available categories
        print("\nAvailable Categories:")
        for category in unique_categories:
            print(f"- {category}")

        # Get user input for category search
        category = input("\nEnter category: ").strip()
        results = store_service.search_product_by_category(category)

        # Show results
        print("\n".join(str(prod) for prod in results) if results else "No products found in this category.")

    elif choice == "3":
        try:
            pid = input("Enter product ID: ").strip()
            qty = input("Enter quantity: ").strip()

            # Validate numeric input
            if not pid.isdigit() or not qty.isdigit():
                raise ValueError("Product ID and Quantity must be numeric values.")

            pid, qty = int(pid), int(qty)

            # Validate positive numbers
            if pid <= 0 or qty <= 0:
                raise ValueError("Product ID and Quantity must be positive values.")

            store_service.add_product_to_cart(cart, pid, qty)

        except ValueError as ve:
            print(ve)
        except ItemOutOfStock as e:
            print(e)  # Handle out-of-stock errors

    elif choice == "4":
        # Show current cart contents before removing
        if not cart.dict_product_quantity:
            print("Cart is empty! Nothing to remove.")
            continue  # Go back to menu

        print("\n🛒 Your Cart:")
        for product_id, quantity in cart.dict_product_quantity.items():
            product = store.product_list.get(product_id)
            print(f"{product.name} x {quantity}")

        try:
            pid = input("Enter product ID to remove: ").strip()
            qty = input("Enter quantity to remove: ").strip()

            # Validate input (should be a number and positive)
            if not pid.isdigit() or not qty.isdigit():
                raise ValueError("Product ID and Quantity must be numbers.")

            pid, qty = int(pid), int(qty)
            if pid <= 0 or qty <= 0:
                raise ValueError("Product ID and Quantity must be positive numbers.")

            # Ensure product is actually in cart
            if pid not in cart.dict_product_quantity:
                print("Product not found in cart.")
                continue

            # Perform removal
            store_service.remove_product_from_cart(cart, pid, qty)

        except ValueError as ve:
            print(ve)

    elif choice == "5":
        if not cart.dict_product_quantity:
            print("Your cart is empty! Add items before purchasing.")
            continue

        print("\n🛒 Processing your purchase...")
        store_service.purchase(cart, customer)
        print("Purchase successful! Thank you for shopping with us.")

    elif choice == "6":
        print("Exiting the application. Thank you for shopping with us!")
        break

    else:
        print("Invalid choice! Please enter a number between 1-6.")

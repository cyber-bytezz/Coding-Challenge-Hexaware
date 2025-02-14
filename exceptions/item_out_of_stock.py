class ItemOutOfStock(Exception):
    """Exception raised when a product is out of stock."""

    def __init__(self, message="Item is out of stock."):
        super().__init__(message)

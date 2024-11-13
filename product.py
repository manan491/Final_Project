# product.py

class Product:
    """Represents a product in the inventory with basic details."""

    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def display_product(self):
        """Displays product details in a readable format."""
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price}, Stock: {self.stock_quantity}"

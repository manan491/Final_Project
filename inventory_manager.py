# inventory_manager.py

from product import Product

# Dictionary to store products by product_id
products = {}

def add_product():
    """Allows Admins to add a new product to the inventory."""
    try:
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        stock_quantity = int(input("Enter stock quantity: "))

        new_product = Product(product_id, name, category, price, stock_quantity)
        products[product_id] = new_product
        print(f"Product '{name}' added successfully!")
    except ValueError:
        print("Error: Please enter valid numbers for price and stock.")
    except Exception:
        print("An unexpected error occurred while adding the product.")

def view_all_products():
    """Displays all products in the inventory."""
    if not products:
        print("Inventory is empty.")
    else:
        for product in products.values():
            print(product.display_product())  # Using display_product method to show product details

def search_product_by_name(name):
    """Searches for a product by name and displays it if found."""
    found = False
    for product in products.values():
        if product.name.lower() == name.lower():
            print(product.display_product())
            found = True
    if not found:
        print("Product not found.")

def update_product(product_id):
    """Allows Admins to update details of an existing product."""
    product = products.get(product_id)
    if not product:
        print("Product not found.")
        return

    try:
        new_name = input(f"Enter new name (current: {product.name}): ") or product.name
        new_category = input(f"Enter new category (current: {product.category}): ") or product.category
        new_price = input(f"Enter new price (current: {product.price}): ")
        new_stock = input(f"Enter new stock quantity (current: {product.stock_quantity}): ")

        product.name = new_name
        product.category = new_category
        product.price = float(new_price) if new_price else product.price
        product.stock_quantity = int(new_stock) if new_stock else product.stock_quantity

        print("Product updated successfully!")
    except ValueError:
        print("Error: Please enter valid numbers for price and stock.")
    except Exception:
        print("An unexpected error occurred while updating the product.")

def delete_product(product_id):
    """Allows Admins to delete a product from the inventory."""
    if product_id in products:
        del products[product_id]
        print(f"Product {product_id} deleted successfully!")
    else:
        print("Product not found.")

# main.py

from user_auth import login
from inventory_manager import add_product, view_all_products, search_product_by_name, update_product, delete_product

def main_menu():
    """Displays the main menu with options based on user role."""
    
    role = login()  # Log in to get the user role
    if not role:
        print("Login failed. Exiting program.")
        return

    while True:
        print("\n--- Inventory Management System ---")
        if role == "Admin":
            print("1. Add a product")
            print("2. View all products")
            print("3. Search product by name")
            print("4. Update a product")
            print("5. Delete a product")
            print("6. Exit")
        else:
            print("1. View all products")
            print("2. Search product by name")
            print("3. Exit")
        
        choice = input("Select an option: ")
        
        try:
            if role == "Admin":
                if choice == "1":
                    add_product()
                elif choice == "2":
                    view_all_products()
                elif choice == "3":
                    name = input("Enter product name to search: ")
                    search_product_by_name(name)
                elif choice == "4":
                    product_id = input("Enter product ID to update: ")
                    update_product(product_id)
                elif choice == "5":
                    product_id = input("Enter product ID to delete: ")
                    delete_product(product_id)
                elif choice == "6":
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            else:  # For Users
                if choice == "1":
                    view_all_products()
                elif choice == "2":
                    name = input("Enter product name to search: ")
                    search_product_by_name(name)
                elif choice == "3":
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
        except Exception:
            print("An error occurred while processing your request.")

# Run the main menu if this file is executed directly
if __name__ == "__main__":
    main_menu()

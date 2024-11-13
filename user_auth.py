# user_auth.py

# Hardcoded users and their roles
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "user": {"password": "user123", "role": "User"}
}

def login():
    """Prompts the user for login credentials and returns their role if valid."""
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login successful! Role: {role}")
            return role
        else:
            print("Invalid username or password.")
            return None
    except Exception:
        print("An error occurred during login.")
        return None

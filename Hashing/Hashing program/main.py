import hashlib


user_database = {} #a  dict for DB

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Function to register a new user
def register_user(username, password):
    if username in user_database:
        print("Error: Username already exists!")
        return
    hashed_password = hash_password(password)
    user_database[username] = hashed_password
    print(f"User '{username}' registered successfully.")

# Function to authenticate a user
def authenticate_user(username, password):
    if username not in user_database:
        print("Error: Username not found.")
        return False
    hashed_password = hash_password(password)
    if user_database[username] == hashed_password:
        print("Authentication successful!")
        return True
    else:
        print("Error: Incorrect password.")
        return False

# Main program
def main():
    while True:
        print("\n--- User Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            authenticate_user(username, password)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()

# Andrew Torres CIS 261

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def create_user_info_file():
    try:
        with open("user_info.txt", "a") as file:
            pass  
    except FileNotFoundError:
        with open("user_info.txt", "w") as file:
            pass  

def read_existing_records():
    user_ids = []
    try:
        with open("user_info.txt", "r") as file:
            for line in file:
                user_id, _, _ = line.strip().split('|')
                user_ids.append(user_id)
    except FileNotFoundError:
        pass  
    return user_ids

def enter_user_information():
    create_user_info_file()
    user_ids = read_existing_records()
    
    while True:
        user_id = input("Enter User ID (or 'End' to terminate): ")
        if user_id.lower() == 'end':
            break

        if user_id in user_ids:
            print("User ID already exists. Please choose another.")
            continue

        password = input("Enter Password: ")
        authorization_code = input("Enter Authorization Code (Admin/User): ")
        
        if authorization_code.lower() not in ['admin', 'user']:
            print("Invalid Authorization Code. Please enter 'Admin' or 'User'.")
            continue

        with open("user_info.txt", "a") as file:
            file.write(f"{user_id}|{password}|{authorization_code}\n")

        user_ids.append(user_id)

def display_user_information():
    try:
        with open("user_info.txt", "r") as file:
            for line in file:
                user_id, password, authorization_code = line.strip().split('|')
                print(f"User ID: {user_id}, Password: {password}, Authorization Code: {authorization_code}")
    except FileNotFoundError:
        print("No user information found.")

def login_process():
    user_info = []
    
    try:
        with open("user_info.txt", "r") as file:
            for line in file:
                user_id, password, authorization_code = line.strip().split('|')
                user_info.append(Login(user_id, password, authorization_code))
    except FileNotFoundError:
        print("User information file not found.")
        return
    
    entered_user_id = input("Enter User ID: ")
    
    found_user = None
    for user in user_info:
        if user.user_id == entered_user_id:
            found_user = user
            break
    
    if not found_user:
        print("User ID not found.")
        return
    
    entered_password = input("Enter Password: ")
    
    if found_user.password == entered_password:
        print(f"Login successful. User ID: {found_user.user_id}, Authorization Code: {found_user.authorization}")
        if found_user.authorization.lower() == 'admin':
            print("You have admin access.")  # Add admin functionality here
        else:
            print("You have user access.")  # Add user functionality here
    else:
        print("Password incorrect.")

if __name__ == "__main__":
    while True:
        print("1. Create and Manage User Information")
        print("2. Login")
        print("3. Display User Information")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            enter_user_information()
        elif choice == "2":
            login_process()
        elif choice == "3":
            display_user_information()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


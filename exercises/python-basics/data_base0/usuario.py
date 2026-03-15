import json
import os

DATA_FOLDER = r"exercises\python-basics\data_base0\data"
FILE_PATH = os.path.join(DATA_FOLDER, "registro.json")

def ensure_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)


def load_users():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def add_user(users):
    name = input("Name: ")
    if name.strip() == "":
        print("Name cannot be empty.")
        return users
    if any(user["name"].lower() == name.lower() for user in users):
        print("User already exists.")
        return users

    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        return users
    email = input("Email: ")
    if email.strip() == "":
        print("Email cannot be empty.")
        return users 
    if not "@" in email or not "." in email:
        print("Invalid email format.")
        return users

    user = {
        "name": name,
        "age": age,
        "email": email
    }

    users.append(user)

    print(name, "has been added.")

    return users


def list_users(users):
    if not users:
        print("No users registered.")
        return
    print("Registered Users:")
    for user in users:
        print(f"""{user['name']},' | ' {user['age']} years,' | 'email: {user['email']}""")

def search_user(users):
    name = input("Name to search: ")

    for user in users:
        if user["name"].lower() == name.lower():
            print(f"""
User found.
{user['name']}, {user['age']} years, email: {user['email']}
""")
            return

    print("User not found.")

def delete_user(users):
    name = input("Name to delete: ")

    for user in users:
        if user["name"].lower() == name.lower():
            print(f"""
                  User found.
                  Deleting {name}," | " {user['age']} years," | " email: {user['email']}
""")
            users.remove(user)
            print(name, "has been deleted.")
            return users

    print("User not found.")
    return users
def update_user(users):
    name = input("Name to update: ")

    for user in users:
        if user["name"].lower() == name.lower():
            print(f"""
                  User found.
                  Updating {name}," | " {user['age']} years," | " email: {user['email']}
""")
            try:
                age = int(input("New Age: "))
            except ValueError:
                print("Invalid age.")
                return users
            email = input("New Email: ")
            if email.strip() == "":
                print("Email cannot be empty.")
                return users 
            if not "@" in email or not "." in email:
                print("Invalid email format.")
                return users

            user["age"] = age
            user["email"] = email
            print(name, "has been updated.")
            return users

    print("User not found.")
    return users


def main():
    ensure_data_folder()

    users = load_users()

    while True:

        print("\n1 - Add user")
        print("2 - List users")
        print("3 - Search user")
        print("4 - Update user")
        print("5 - Delete user")
        print("6 - Exit")

        option = input("Choose: ")

        if option == "1":
            users = add_user(users)
            save_users(users)

        elif option == "2":
            list_users(users)

        elif option == "3":
            search_user(users)
        elif option == "4":
            users = update_user(users)
            save_users(users)
        elif option == "5":
            users = delete_user(users)
            save_users(users)
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


main()
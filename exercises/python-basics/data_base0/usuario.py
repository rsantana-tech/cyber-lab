import json
import os

DATA_FOLDER = r"exercises\python-basics\data_base0\data"
FILE_PATH = os.path.join(DATA_FOLDER, "registro.json")


def ensure_data_folder():
    os.makedirs(DATA_FOLDER, exist_ok=True)


def load_users():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []


def save_users(users):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)


def is_valid_email(email):
    email = email.strip()

    if email == "":
        return False
    if "@" not in email or "." not in email:
        return False
    if email.count("@") != 1:
        return False

    local_part, domain_part = email.split("@")

    if local_part == "" or domain_part == "":
        return False
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False

    return True


def user_exists_by_name(users, name):
    return any(user["name"].strip().lower() == name.strip().lower() for user in users)


def email_exists(users, email, current_user=None):
    for user in users:
        if current_user is not None and user is current_user:
            continue
        if user["email"].strip().lower() == email.strip().lower():
            return True
    return False


def add_user(users):
    name = input("Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return users

    if user_exists_by_name(users, name):
        print("User already exists.")
        return users

    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age cannot be negative.")
            return users
    except ValueError:
        print("Invalid age.")
        return users

    email = input("Email: ").strip()

    if not is_valid_email(email):
        print("Invalid email format.")
        return users

    if email_exists(users, email):
        print("Email already exists.")
        return users

    user = {
        "name": name,
        "age": age,
        "email": email,
    }

    users.append(user)
    print(f"{name} has been added.")
    return users


def list_users(users):
    if not users:
        print("No users registered.")
        return

    print("\nRegistered users:")
    for index, user in enumerate(users, start=1):
        print(
            f"{index}. Name: {user['name']} | Age: {user['age']} years | Email: {user['email']}"
        )


def search_user(users):
    name = input("Name to search: ").strip()

    for user in users:
        if user["name"].strip().lower() == name.lower():
            print("\nUser found:")
            print(
                f"Name: {user['name']} | Age: {user['age']} years | Email: {user['email']}"
            )
            return

    print("User not found.")


def delete_user(users):
    name = input("Name to delete: ").strip()

    for user in users:
        if user["name"].strip().lower() == name.lower():
            print("\nUser found:")
            print(
                f"Name: {user['name']} | Age: {user['age']} years | Email: {user['email']}"
            )
            users.remove(user)
            print("User removed successfully.")
            return users

    print("User not found.")
    return users


def update_user(users):
    name = input("Name to update: ").strip()

    for user in users:
        if user["name"].strip().lower() == name.lower():
            print("\nUser found:")
            print(
                f"Name: {user['name']} | Age: {user['age']} years | Email: {user['email']}"
            )

            new_name = input("New name: ").strip()
            if new_name == "":
                print("Name cannot be empty.")
                return users

            if new_name.lower() != user["name"].strip().lower() and user_exists_by_name(users, new_name):
                print("Another user with this name already exists.")
                return users

            try:
                new_age = int(input("New age: "))
                if new_age < 0:
                    print("Age cannot be negative.")
                    return users
            except ValueError:
                print("Invalid age.")
                return users

            new_email = input("New email: ").strip()
            if not is_valid_email(new_email):
                print("Invalid email format.")
                return users

            if email_exists(users, new_email, current_user=user):
                print("Another user with this email already exists.")
                return users

            user["name"] = new_name
            user["age"] = new_age
            user["email"] = new_email

            print("User updated successfully.")
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

        option = input("Choose: ").strip()

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

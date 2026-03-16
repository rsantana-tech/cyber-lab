import json
import os

BASE_PATH = os.path.dirname(__file__)
FILE_NAME = os.path.join(BASE_PATH, "users.json")


def load_users():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w") as file:
            json.dump([], file)

        return []

    with open(FILE_NAME, "r") as file:
        try:
            users = json.load(file)
            return users
        except:
            return []


def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)


def add_user(users):
    name = input("Name: ")
    age = int(input("Age: "))
    city = input("City: ")

    user = {
        "name": name,
        "age": age,
        "city": city
    }

    users.append(user)

    print("User added.")


def list_users(users):
    if len(users) == 0:
        print("No users registered.")
        return

    for i, user in enumerate(users, start=1):
        print(f"{i}. name: {user['name']}, age: {user['age']}, city: {user['city']}")


def find_user(users):
    name = input("Enter name to search: ")

    for user in users:
        if user["name"].lower() == name.lower():
            print("User found:", f"name: {user['name']}, age: {user['age']}, city: {user['city']}")
            return

    print("User not found.")

def delete_user(users):
    name = input("Enter name to delete: ")

    for user in users:
        if user["name"].lower() == name.lower():
            users.remove(user)
            print("User deleted.")
            return

    print("User not found.")


def main():

    users = load_users()

    while True:

        print("\nMENU")
        print("1 - Add user")
        print("2 - List users")
        print("3 - Find user")
        print("4 - Delete user")
        print("5 - Exit")

        option = input("Choose: ")

        if option == "1":
            add_user(users)
            save_users(users)

        elif option == "2":
            list_users(users)

        elif option == "3":
            find_user(users)

        elif option == "4":
            delete_user(users)
            save_users(users)

        elif option == "5":
            save_users(users)
            break

        else:
            print("Invalid option")


main()
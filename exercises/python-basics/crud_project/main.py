from services.user_service import load_users, save_users, add_user, list_users, find_user, update_user, delete_user


def main():
    users = load_users()

    while True:
        print("\nMENU")
        print("1 - Add user")
        print("2 - List users")
        print("3 - Find user")
        print("4 - Delete user")
        print("5 - Update user")
        print("6 - Exit")

        option = input("Choose: ")

        if option == "1":
            name = input("Name: ")
            try:
                age = int(input("Age: "))
                if age <= 0 or age > 150:
                    print("Invalid age. Must be between 1 and 150.")
                    continue
            except ValueError:
                print("Invalid age. Please enter a number.")
                continue
            city = input("City: ")
            add_user(users, name, age, city)
            save_users(users)
            print("User added.")

        elif option == "2":
            users_list = list_users(users)
            if not users_list:
                print("No users registered.")
            else:
                print("Registered users:")
                for user in users_list:
                    print(f"ID: {user['id']}. name: {user['name']} | age: {user['age']} | city: {user['city']}")

        elif option == "3":
            try:
                user_id = int(input("Enter ID to search: "))
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue
            user = find_user(users, user_id)
            if user:
                print(f"ID: {user['id']}. name: {user['name']} | age: {user['age']} | city: {user['city']}")
            else:
                print("User not found.")

        elif option == "4":
            try:
                user_id = int(input("Enter ID to delete: "))
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue
            if delete_user(users, user_id):
                print("User deleted.")
                save_users(users)
            else:
                print("User not found.")

        elif option == "5":
            try:
                user_id = int(input("Enter ID to update: "))
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue
            name = input("New name: ")
            try:
                age = int(input("New age: "))
                if age <= 0 or age > 150:
                    print("Invalid age. Must be between 1 and 150.")
                    continue
            except ValueError:
                print("Invalid age. Please enter a number.")
                continue
            city = input("New city: ")
            if update_user(users, user_id, name, age, city):
                print("User updated.")
                save_users(users)
            else:
                print("User not found.")
        elif option == "6":
            save_users(users)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
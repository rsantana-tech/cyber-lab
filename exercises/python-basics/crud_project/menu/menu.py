from services.user_service import add_user, list_users, find_user, update_user, delete_user


def show_menu():
    print("1. Add User")
    print("2. List Users")
    print("3. Find User")
    print("4. Update User")
    print("5. Delete User")
    print("6. Exit")

def menu():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_user()
            elif choice == '2':
                list_users()
            elif choice == '3':
                find_user()
            elif choice == '4':
                update_user()
            elif choice == '5':
                delete_user()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: Invalid input. Please enter a valid number. Details: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        print()  # Linha em branco para melhor legibilidade


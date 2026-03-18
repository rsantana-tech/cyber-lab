from repositories.user_repository import load_users, save_users
from validators.user_validator import validate_user_input


def _prompt_int(prompt: str):
    """Solicita um número inteiro ao usuário.

    Retorna o inteiro ou None se a entrada for inválida.
    """
    try:
        return int(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def _prompt_optional_int(prompt: str):
    """Solicita um número inteiro opcional ao usuário."""
    value = input(prompt).strip()
    if value == "":
        return None

    try:
        return int(value)
    except ValueError:
        print("Error: Please enter a valid number or leave blank.")
        return None


def _find_user_by_id(users, user_id):
    return next((user for user in users if user["id"] == user_id), None)


def add_user():
    users = load_users()
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    age = _prompt_int("Enter user age: ")
    if age is None:
        return

    is_valid, error = validate_user_input(name, email, age)
    if not is_valid:
        print(f"Error: {error}")
        return

    user_id = max([user["id"] for user in users], default=0) + 1
    users.append({"id": user_id, "name": name, "email": email, "age": age})
    save_users(users)
    print("User added successfully.")


def list_users():
    users = load_users()
    if not users:
        print("No users found.")
        return

    for user in users:
        age = user.get("age", "N/A")
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Age: {age}")


def find_user():
    user_id = _prompt_int("Enter user ID to find: ")
    if user_id is None:
        return

    users = load_users()
    user = _find_user_by_id(users, user_id)
    if user:
        age = user.get("age", "N/A")
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Age: {age}")
    else:
        print("User not found.")


def update_user():
    user_id = _prompt_int("Enter user ID to update: ")
    if user_id is None:
        return

    users = load_users()
    user = _find_user_by_id(users, user_id)
    if not user:
        print("User not found.")
        return

    name = input(f"Enter new name (current: {user['name']}): ")
    email = input(f"Enter new email (current: {user['email']}): ")
    age = _prompt_optional_int(f"Enter new age (current: {user.get('age', 'N/A')}): ")

    # Validar apenas se novos valores foram fornecidos
    if name or email or age is not None:
        new_name = name or user["name"]
        new_email = email or user["email"]
        new_age = age if age is not None else user.get("age")

        is_valid, error = validate_user_input(new_name, new_email, new_age)
        if not is_valid:
            print(f"Error: {error}")
            return

        user["name"] = new_name
        user["email"] = new_email
        if new_age is not None:
            user["age"] = new_age

        save_users(users)
        print("User updated successfully.")
    else:
        print("No changes provided.")


def delete_user():
    user_id = _prompt_int("Enter user ID to delete: ")
    if user_id is None:
        return

    users = load_users()
    user = _find_user_by_id(users, user_id)
    if not user:
        print("User not found.")
        return

    users.remove(user)
    save_users(users)
    print("User deleted successfully.")








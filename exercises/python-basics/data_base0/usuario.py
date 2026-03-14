import os
import json

# Pasta do próprio arquivo .py
base_path = os.path.dirname(__file__)

# Pasta de dados
data_folder = os.path.join(base_path, "data")
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

# Arquivo JSON
file_path = os.path.join(data_folder, "registro.json")


def load_people():
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_people(people):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(people, file, indent=4, ensure_ascii=False)


def show_menu():
    print("\n--- MENU ---")
    print("1 - Add person")
    print("2 - List people")
    print("3 - Search person")
    print("4 - Update age")
    print("5 - Delete person")
    print("0 - Exit")

    try:
        return int(input("Choose an option: ").strip())
    except ValueError:
        return -1


def add_person(people):
    print("\n--- Add person ---")
    name = input("Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    for person in people:
        if person["name"].lower() == name.lower():
            print("This person is already registered.")
            return

    try:
        age = int(input("Age: ").strip())
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    people.append({
        "name": name,
        "age": age
    })

    save_people(people)
    print(f"{name} has been added.")


def list_people(people):
    print("\n--- List people ---")

    if not people:
        print("No people registered.")
        return

    for index, person in enumerate(people, start=1):
        print(f"{index} - Name: {person['name']} | Age: {person['age']}")


def search_person(people):
    print("\n--- Search person ---")
    search_name = input("Name to search: ").strip()

    if not search_name:
        print("Name cannot be empty.")
        return

    for person in people:
        if person["name"].lower() == search_name.lower():
            print(f"Person found: Name = {person['name']}, Age = {person['age']}")
            return

    print("Person not found.")


def update_age(people):
    print("\n--- Update age ---")
    search_name = input("Name to update: ").strip()

    if not search_name:
        print("Name cannot be empty.")
        return

    for person in people:
        if person["name"].lower() == search_name.lower():
            try:
                new_age = int(input("New age: ").strip())
            except ValueError:
                print("Invalid age. Please enter a number.")
                return

            person["age"] = new_age
            save_people(people)
            print(f"Age updated for {person['name']}.")
            return

    print("Person not found.")


def delete_person(people):
    print("\n--- Delete person ---")
    search_name = input("Name to delete: ").strip()

    if not search_name:
        print("Name cannot be empty.")
        return

    for index, person in enumerate(people):
        if person["name"].lower() == search_name.lower():
            deleted_name = person["name"]
            del people[index]
            save_people(people)
            print(f"{deleted_name} has been deleted.")
            return

    print("Person not found.")


def main():
    people = load_people()

    while True:
        option = show_menu()

        if option == 1:
            add_person(people)
        elif option == 2:
            list_people(people)
        elif option == 3:
            search_person(people)
        elif option == 4:
            update_age(people)
        elif option == 5:
            delete_person(people)
        elif option == 0:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
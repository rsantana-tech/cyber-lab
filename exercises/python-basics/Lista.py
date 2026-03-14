# CRUD with list of dictionaries

people = []


def options():
    print("\n1 - Add person")
    print("2 - List people")
    print("3 - Search person")
    print("4 - Update age")
    print("5 - Delete person")
    print("0 - Exit")

    try:
        return int(input("Choose an option: "))
    except ValueError:
        return -1


def add_person():
    print("\nCreate")
    name = input("Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    for person in people:
        if person["name"].lower() == name.lower():
            print("This person is already registered.")
            return

    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        return

    people.append({
        "name": name,
        "age": age
    })

    print(f"{name} has been added.")


def list_people():
    print("\nRead")

    if not people:
        print("No people registered.")
        return

    for i, person in enumerate(people):
        print(f"{i} - {person['name']} - {person['age']}")
        print("-" * 20)


def search_person():
    print("\nSearch")
    search_name = input("Name to search: ").strip()

    found = False

    for person in people:
        if person["name"].lower() == search_name.lower():
            print(f"Name: {person['name']}, Age: {person['age']}")
            found = True
            break

    if not found:
        print("Person not found.")


def update_age():
    print("\nUpdate")
    search_name = input("Name to update: ").strip()

    for person in people:
        if person["name"].lower() == search_name.lower():
            try:
                new_age = int(input("New age: "))
            except ValueError:
                print("Invalid age.")
                return

            person["age"] = new_age
            print(f"Age updated for {person['name']} to {person['age']}")
            return

    print("Person not found.")


def delete_person():
    print("\nDelete")
    search_name = input("Name to delete: ").strip()

    for i, person in enumerate(people):
        if person["name"].lower() == search_name.lower():
            deleted_name = person["name"]
            del people[i]
            print(f"{deleted_name} has been deleted.")
            return

    print("Person not found.")


if __name__ == "__main__":
    while True:
        option = options()

        if option == 1:
            add_person()
        elif option == 2:
            list_people()
        elif option == 3:
            search_person()
        elif option == 4:
            update_age()
        elif option == 5:
            delete_person()
        elif option == 0:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
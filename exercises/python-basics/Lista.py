form = []
while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    form.append({"name":name,
                  "age": age})

    continue_input = input("Do you want to add another person? (yes/no): ").strip().lower()
    if continue_input != "yes":
        break
print("\nList of people in the form:")
for person in form:
    print(f"Name: {person['name']}, Age: {person['age']}")
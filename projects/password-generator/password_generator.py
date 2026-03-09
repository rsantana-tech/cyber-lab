import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Cyber Lab - Password Generator")

    length = int(input("Enter desired password length: "))

    password = generate_password(length)

    print("\nGenerated password:")
    print(password)


if __name__ == "__main__":
    main()
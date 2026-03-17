import os
import json

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_PATH, "data", "users.json")

def load_users():
    os.makedirs(os.path.dirname(FILE_NAME), exist_ok=True)
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)
        return []

    with open(FILE_NAME, "r") as file:
        try:
            users = json.load(file)
            return users
        except json.JSONDecodeError:
            return []
        

def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)


def add_user(users, name, age, city):
    user = {
        "id": max(user["id"] for user in users) + 1 if users else  1,
        "name": name,
        "age": age,
        "city": city
    }

    users.append(user)


def list_users(users):
    return users

def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def delete_user(users, user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return True
    return False

def update_user(users, user_id, name, age, city):
    for user in users:
        if user["id"] == user_id:
            user['name'] = name
            user['age'] = age
            user['city'] = city
            return True
    return False





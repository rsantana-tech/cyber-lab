import json
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parents[1] / "data" / "users.json"

def load_users():
    if not BASE_PATH.exists():
        return []

    try:
        if BASE_PATH.stat().st_size == 0:
            return []

        with BASE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if data else []
    except json.JSONDecodeError:
        # Arquivo vazio ou JSON inválido
        return []


def save_users(users):
    BASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with BASE_PATH.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

if __name__ == "__main__":
    # Apenas para testes rápidos; não roda em importações
    load_users()
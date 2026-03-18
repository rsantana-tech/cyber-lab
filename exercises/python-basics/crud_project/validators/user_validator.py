import re


def validate_name(name):
    """Valida nome do usuário"""
    if not name or len(name.strip()) < 2:
        return False, "Name must be at least 2 characters."
    if not name.replace(" ", "").isalpha():
        return False, "Name must contain only letters and spaces."
    return True, None


def validate_email(email):
    """Valida email do usuário"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Invalid email format."
    return True, None


def validate_age(age):
    """Valida idade do usuário"""
    try:
        age_int = int(age)
    except (TypeError, ValueError):
        return False, "Age must be a number."

    if age_int < 0:
        return False, "Age cannot be negative."
    if age_int > 150:
        return False, "Age seems unrealistic."

    return True, None


def validate_user_input(name, email, age):
    """Valida nome, email e idade juntos"""
    is_valid, error = validate_name(name)
    if not is_valid:
        return False, error

    is_valid, error = validate_email(email)
    if not is_valid:
        return False, error

    is_valid, error = validate_age(age)
    if not is_valid:
        return False, error

    return True, None

from typing import Dict


# Temporary in-memory user storage
# Later, this can be replaced with your project's database.
users: Dict[str, dict] = {}


def signup(name: str, email: str, password: str, confirm_password: str):
    """Create a new user account."""

    if not name or not email or not password:
        return False, "Please fill in all fields."

    if password != confirm_password:
        return False, "Passwords do not match."

    if email in users:
        return False, "An account with this email already exists."

    users[email] = {
        "name": name,
        "password": password,
    }

    return True, "Account created successfully."


def login(email: str, password: str):
    """Check user login credentials."""

    if email not in users:
        return False, "Account not found."

    if users[email]["password"] != password:
        return False, "Incorrect password."

    return True, f"Welcome, {users[email]['name']}!"
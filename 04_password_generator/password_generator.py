"""
Password Generator (CLI)

Author: Madeshwaran
"""
import secrets
import string

CHARACTERS = string.ascii_letters + string.digits + "!@#$%^&*"
MIN_LENGTH = 4


def validate_length(length_text: str) -> int:
    """
    Parse and validate a password length string.
    Raises ValueError if not a whole number or below MIN_LENGTH.
    """
    try:
        length = int(length_text)
    except ValueError:
        raise ValueError("Please enter a whole number.")
    if length < MIN_LENGTH:
        raise ValueError(f"Use at least {MIN_LENGTH} characters.")
    return length


def generate_password(length: int, characters: str = CHARACTERS) -> str:
    """Generate a cryptographically secure random password of the given length."""
    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:
    length_text = input("Password length: ")
    try:
        length = validate_length(length_text)
    except ValueError as e:
        print(e)
        raise SystemExit

    password = generate_password(length)
    print("Generated password:")
    print(password)


if __name__ == "__main__":
    main()

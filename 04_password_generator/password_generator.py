import secrets
import string

length_text = input("Password length: ")

try:
    length = int(length_text)
except ValueError:
    print("Please enter a whole number.")
    raise SystemExit

if length < 4:
    print("Use at least 4 characters.")
    raise SystemExit

characters = string.ascii_letters + string.digits + "!@#$%^&*"

password = "".join(secrets.choice(characters) for _ in range(length))

print("Generated password:")
print(password)

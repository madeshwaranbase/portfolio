def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


print("Simple Calculator")
print("-----------------")

while True:
    try:
        first_number = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        if operator == "+":
            result = add(first_number, second_number)
        elif operator == "-":
            result = subtract(first_number, second_number)
        elif operator == "*":
            result = multiply(first_number, second_number)
        elif operator == "/":
            result = divide(first_number, second_number)
            if result is None:
                print("Cannot divide by zero.")
                continue
        else:
            print("Invalid operator.")
            continue

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")

    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() != "y":
        print("Calculator closed.")
        break

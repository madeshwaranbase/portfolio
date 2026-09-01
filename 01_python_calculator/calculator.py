"""
Simple CLI calculator with core arithmetic operations.

Author: Madeshwaran
"""


class DivisionByZeroError(Exception):
    """Raised when attempting to divide by zero."""
    pass


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises DivisionByZeroError if b is 0."""
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(first_number: float, operator: str, second_number: float) -> float:
    """Dispatch to the correct operation. Raises ValueError for unknown operators."""
    if operator not in OPERATIONS:
        raise ValueError(f"Invalid operator: {operator}")
    return OPERATIONS[operator](first_number, second_number)


def main() -> None:
    print("Simple Calculator")
    print("-----------------")
    while True:
        try:
            first_number = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            second_number = float(input("Enter second number: "))
            result = calculate(first_number, operator, second_number)
            print("Result:", result)
        except DivisionByZeroError as e:
            print(e)
        except ValueError as e:
            print(f"Invalid input: {e}")

        if input("Calculate again? (y/n): ").strip().lower() != "y":
            print("Calculator closed.")
            break


if __name__ == "__main__":
    main()

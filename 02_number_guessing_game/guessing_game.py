"""
Number Guessing Game (CLI)

Author: Madeshwaran
"""
import random


def check_guess(guess: int, secret_number: int) -> str:
    """
    Compare a guess to the secret number.
    Returns "low", "high", or "correct".
    """
    if guess < secret_number:
        return "low"
    if guess > secret_number:
        return "high"
    return "correct"


def get_random_number(low: int = 1, high: int = 100) -> int:
    """Return a random integer between low and high, inclusive."""
    return random.randint(low, high)


def main() -> None:
    secret_number = get_random_number(1, 100)
    attempts = 0

    print("Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1
        result = check_guess(guess, secret_number)

        if result == "low":
            print("Too low.")
        elif result == "high":
            print("Too high.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()

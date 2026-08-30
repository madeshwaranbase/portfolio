import random

secret_number = random.randint(1, 100)
attempts = 0

print("Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a whole number.")

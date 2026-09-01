# Number Guessing Game (CLI)

A CLI number-guessing game where the player guesses a randomly generated number between 1–100, with core logic separated from I/O for full test coverage.

## Why this project

Project 02 of a 20-project Python/Selenium portfolio. Demonstrates refactoring random/interactive logic into pure, testable functions — the same separation-of-concerns pattern used in real test automation frameworks.

## Features

- Pure `check_guess()` function (no I/O) — fully testable
- Configurable random range via `get_random_number(low, high)`
- Input validation with retry loop
- 11 unit tests (pytest, parametrized) covering boundaries and randomness bounds

## Tech stack

- Python 3.12
- pytest

## Project structure

```
02_number_guessing_game/
├── game.py         # core logic + CLI loop
├── test_game.py    # pytest suite
└── README.md
```

## How to run

```bash
# Play the game
python3 game.py

# Run the tests
pip install pytest
pytest test_game.py -v
```

## Sample run

```
Number Guessing Game
I'm thinking of a number between 1 and 100.
Your guess: 50
Too high.
Your guess: 25
Too low.
Your guess: 37
Correct! You got it in 3 attempts.
```

## Test results

```
11 passed in 0.02s
```

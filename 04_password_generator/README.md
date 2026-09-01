# Password Generator (CLI)

A CLI tool that generates cryptographically secure random passwords, with validation and generation logic fully unit-tested.

## Why this project

Project 04 of a 20-project Python/Selenium portfolio. Demonstrates use of `secrets` (not `random`) for security-sensitive generation, and testing randomized output — asserting on character-set membership and length rather than exact values, since exact output can't be predicted.

## Features

- Uses `secrets.choice()` for cryptographically secure randomness
- Length validation with clear, distinct error messages
- Configurable character set via function parameter
- 10 unit tests (pytest) covering validation edge cases and randomized-output properties

## Tech stack

- Python 3.12
- pytest

## Project structure

```
04_password_generator/
├── password_generator.py         # core logic + CLI
├── test_password_generator.py    # pytest suite
└── README.md
```

## How to run

```bash
# Generate a password
python3 password_generator.py

# Run the tests
pip install pytest
pytest test_password_generator.py -v
```

## Sample run

```
Password length: 16
Generated password:
xT9#kLp2@fQ7&mZs
```

## Test results

```
10 passed in 0.02s
```

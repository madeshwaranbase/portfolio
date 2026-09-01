# Simple Calculator (CLI)

A command-line calculator supporting addition, subtraction, multiplication, and division, with a full pytest suite covering core logic and edge cases.

## Why this project

Project 01 of a 20-project Python/Selenium portfolio built to demonstrate QA/SDET fundamentals: clean function design, exception handling, and test coverage from day one — not just working code.

## Features

- Four core operations via a single dispatch table (`OPERATIONS`)
- Custom `DivisionByZeroError` instead of silent `None` returns
- Type-hinted, documented functions
- Input validation with clear error messages
- 13 unit tests (pytest, parametrized) covering happy paths, edge cases, and invalid input

## Tech stack

- Python 3.12
- pytest

## Project structure

```
01_python_calculator/
├── calculator.py         # core logic + CLI loop
├── test_calculator.py    # pytest suite
└── README.md
```

## How to run

```bash
# Run the calculator
python3 calculator.py

# Run the tests
pip install pytest
pytest test_calculator.py -v
```

## Sample run

```
Simple Calculator
-----------------
Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 0
Cannot divide by zero.
Calculate again? (y/n): n
Calculator closed.
```

## Test results

```
13 passed in 0.02s
```

# Learning Guide

Do not treat this repository as a copy-paste exercise.

For every project:

1. Read the README.
2. Type the code yourself if you are learning the concept.
3. Run the program.
4. Try invalid inputs.
5. Change one small part.
6. Break it intentionally.
7. Fix the problem.
8. Commit the working version to Git.
9. Write down what you learned.
10. Move to the next project only when you can explain the code.

## Recommended Git workflow

```bash
git add .
git commit -m "Add project 01 calculator"
git push
```

Use small commits such as:

```text
Add calculator functions
Handle invalid input
Handle division by zero
Add calculator README
```

## Selenium prerequisites

Install Google Chrome and a compatible Selenium 4 package.

Selenium Manager normally handles the browser driver automatically.

Start with:

```bash
pip install selenium pytest
```

Then run:

```bash
pytest -v
```

## Portfolio progression

Projects 1-4: Python fundamentals

Projects 5-7: Practical Python and file processing

Projects 8-10: QA-oriented Python

Projects 11-16: Selenium fundamentals

Projects 17-19: Pytest and test engineering

Project 20: Framework architecture

## Interview preparation

For each project, be able to answer:

- Why did you build it?
- What problem does it solve?
- What Python concepts did you use?
- What can fail?
- How did you handle failures?
- What would you improve?
- Why did you choose this design?

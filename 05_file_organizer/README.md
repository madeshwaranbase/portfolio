# File Organizer (CLI)

A CLI tool that sorts files in a folder into subfolders by type (Images, Documents, Videos, Music, Others), with destructive file operations fully covered by tests.

## Why this project

Project 05 of a 20-project Python/Selenium portfolio. This one performs real file-system moves, so testing it safely matters: every test runs against pytest's `tmp_path` fixture (isolated temp directory, auto-cleaned), never the real filesystem — the same discipline required for automation that reads/writes test fixtures, downloads, or reports.

## Features

- `classify_file()` — pure function mapping extension → category, fully isolated from disk access
- `organize_folder()` — returns a log of actions instead of printing directly, so behavior is assertable
- Safe by default: skips (never overwrites) files that already exist at the destination
- 13 unit tests (pytest) covering classification, moves, collisions, subdirectories, and missing folders

## Tech stack

- Python 3.12
- pytest

## Project structure

```
05_file_organizer/
├── file_organizer.py         # core logic + CLI
├── test_file_organizer.py    # pytest suite
└── README.md
```

## How to run

```bash
# Organize a folder
python3 file_organizer.py

# Run the tests (safe — uses temp directories, never touches real files)
pip install pytest
pytest test_file_organizer.py -v
```

## Sample run

```
Folder to organize: ./Downloads
Moved photo.jpg -> Images
Moved report.pdf -> Documents
Skipped existing file: song.mp3
Organization complete.
```

## Test results

```
13 passed in 0.03s
```

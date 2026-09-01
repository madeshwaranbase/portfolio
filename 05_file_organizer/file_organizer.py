"""
File Organizer (CLI)

Organizes files in a folder into subfolders by type (Images, Documents, Videos, Music, Others).

Author: Madeshwaran
"""
import shutil
from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
}
OTHERS_CATEGORY = "Others"


def classify_file(file_name: str, file_types: dict = FILE_TYPES) -> str:
    """Return the category name for a file based on its extension."""
    suffix = Path(file_name).suffix.lower()
    for category, extensions in file_types.items():
        if suffix in extensions:
            return category
    return OTHERS_CATEGORY


def organize_folder(source: Path) -> list[str]:
    """
    Move each file in `source` into a subfolder based on its type.
    Returns a list of human-readable log messages describing what happened.
    Raises FileNotFoundError if source doesn't exist or isn't a directory.
    """
    if not source.exists() or not source.is_dir():
        raise FileNotFoundError(f"Folder does not exist: {source}")

    log = []
    for file in source.iterdir():
        if not file.is_file():
            continue

        folder_name = classify_file(file.name)
        destination = source / folder_name
        destination.mkdir(exist_ok=True)
        target = destination / file.name

        if target.exists():
            log.append(f"Skipped existing file: {file.name}")
            continue

        shutil.move(str(file), str(target))
        log.append(f"Moved {file.name} -> {folder_name}")

    return log


def main() -> None:
    source = Path(input("Folder to organize: ").strip())
    try:
        log = organize_folder(source)
    except FileNotFoundError as e:
        print(e)
        raise SystemExit

    for line in log:
        print(line)
    print("Organization complete.")


if __name__ == "__main__":
    main()

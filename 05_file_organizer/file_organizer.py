from pathlib import Path
import shutil

SOURCE = Path(input("Folder to organize: ").strip())

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
}

if not SOURCE.exists() or not SOURCE.is_dir():
    print("Folder does not exist.")
    raise SystemExit

for file in SOURCE.iterdir():
    if not file.is_file():
        continue

    folder_name = "Others"

    for category, extensions in FILE_TYPES.items():
        if file.suffix.lower() in extensions:
            folder_name = category
            break

    destination = SOURCE / folder_name
    destination.mkdir(exist_ok=True)

    target = destination / file.name
    if target.exists():
        print(f"Skipped existing file: {file.name}")
        continue

    shutil.move(str(file), str(target))
    print(f"Moved {file.name} -> {folder_name}")

print("Organization complete.")

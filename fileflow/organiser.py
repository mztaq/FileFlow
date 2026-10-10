from pathlib import Path
import shutil
from fileflow.scanner import scan_folder
from fileflow.categories import get_category


def preview_organization(folder_path):
    files=scan_folder(folder_path)
    folder=Path(folder_path)

    for file in files:
        category = get_category(file.name)
        destination = folder / category / file.name

        print(f"{file.name} => {destination}")

def move_file(folder_path):
    files = scan_folder(folder_path)
    folder = Path(folder_path)

    for file in files:
        category = get_category(file.name)
        destination = folder / category / file.name

        if destination.exists():
            print(f"Skipping {file.name}: already exists")
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)

        shutil.move(str(file), str(destination))
        print(f"Moved {file.name} => {category}/")

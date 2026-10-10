from fileflow.scanner import scan_folder
from fileflow.categories import get_category

folder_path=input("Enter the folder path:\n-> ")

try:
    files= scan_folder(folder_path)
    print(f"\nFound {len(files)} files:\n")

    for file in files:
        category = get_category(file.name)
        print(f"{file.name} is {category}")

except (FileNotFoundError, NotADirectoryError) as error:
    print(f"Error: {error}")

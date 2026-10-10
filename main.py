
from fileflow.organiser import preview_organization, move_file

folder_path = input("Enter folder path: ")

try:
    preview_organization(folder_path)

    confirm = input("\nMove these files? (y/n): ")

    if confirm.strip().lower() == "y":
        move_file(folder_path)
    else:
        print("Operation cancelled.")

except (FileNotFoundError, NotADirectoryError) as error:
    print(f"Error: {error}")

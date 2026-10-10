from fileflow.scanner import scan_folder
folder_path=input("Enter the folder path:\n-> ")

try:
    files= scan_folder(folder_path)
    print(f"\nFound {len(files)} files:\n")

    for file in files:
        print(file.name)
except (FileNotFoundError, NotADirectoryError) as error:
    print(f"Error: {error}")

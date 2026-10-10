from pathlib import Path

def scan_folder(folder_path):
    folder=Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError("The folder you entered doesnt exist!")
    if not folder.is_dir():
        raise NotADirectoryError("The path provided isn't a folder!")
    files=[]
    for item in folder.iterdir():
        if item.is_file():
            files.append(item)
    return files

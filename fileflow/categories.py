from pathlib import Path

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Code": [".py", ".rs", ".js", ".java", ".cpp", ".cs" ".html", ".css"]
}


def get_category(filename):
    extension = Path(filename).suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"

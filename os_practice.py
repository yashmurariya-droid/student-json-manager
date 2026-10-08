import os
import shutil

practice_folder = "PracticeDownloads"

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Documents": [".pdf", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Python": [".py"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".js", ".html", ".css", ".java", ".cpp", ".c"]
}


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def get_unique_filename(dest_folder, filename):
    """
    If a file with the same name already exists, create a unique name.
    Example: photo.jpg → photo_1.jpg, photo_2.jpg, etc.
    """
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    
    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_filename


def organize_files(source_folder):

    files = [
        file for file in os.listdir(source_folder)
        if os.path.isfile(os.path.join(source_folder, file))
    ]

    print(f"\nFound {len(files)} files to organize.\n")

    moved_count = 0
    error_count = 0

    for filename in files:

        category = get_category(filename)

        category_folder = os.path.join(source_folder, category)

        os.makedirs(category_folder, exist_ok=True)

        source_path = os.path.join(source_folder, filename)
        
        # Check for duplicates and get unique filename
        dest_filename = get_unique_filename(category_folder, filename)
        destination_path = os.path.join(category_folder, dest_filename)

        # Add error handling with try/except
        try:
            shutil.move(source_path, destination_path)
            
            # Show different message if file was renamed
            if dest_filename != filename:
                print(f"✓ Moved: {filename} -> {category}/{dest_filename} (renamed to avoid duplicate)")
            else:
                print(f"✓ Moved: {filename} -> {category}/")
            
            moved_count += 1
            
        except PermissionError:
            print(f"✗ Error: Permission denied - cannot move '{filename}'")
            error_count += 1
            
        except FileNotFoundError:
            print(f"✗ Error: File not found - '{filename}'")
            error_count += 1
            
        except Exception as e:
            print(f"✗ Error: Could not move '{filename}' - {str(e)}")
            error_count += 1

    print(f"\n✅ Organized {moved_count} files successfully!")
    
    if error_count > 0:
        print(f"⚠️  {error_count} file(s) could not be moved due to errors.")


organize_files(practice_folder)
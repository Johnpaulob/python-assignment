import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    #Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    #Check if destination directory exists
    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    #Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)

        #Skip if it's not a file
        if not os.path.isfile(source_file):
            continue

        dest_file = os.path.join(dest_dir, filename)

        #If file already exists in destination, append timestamp
        if os.path.exists(dest_file):
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            new_filename = f"{name}_{timestamp}{ext}"
            dest_file = os.path.join(dest_dir, new_filename)

        try:
            shutil.copy2(source_file, dest_file)#actual copy function
            print(f"Copied: {filename} -> {dest_file}")
        except Exception as e:
            print(f"Failed to copy '{filename}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    backup_files(source, destination)

    #usuage python Q4-backup_files.py source destination
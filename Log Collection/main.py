import os
import shutil
from datetime import datetime

def collect_logs(source_directories, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for source_directory in source_directories:
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                filepath = os.path.join(root, file)
                if filepath.endswith(".log"):
                    dest_path = os.path.join(destination_directory, os.path.basename(filepath))
                    shutil.copy(filepath, dest_path)
                    print(f"Copied {filepath} to {dest_path}")

if __name__ == "__main__":
    source_directories = ["/var/log", "/path/to/another/log/directory"]  # Remplacez par les répertoires sources
    destination_directory = f"/path/to/central/log/directory/{datetime.now().strftime('%Y-%m-%d')}"
    collect_logs(source_directories, destination_directory)

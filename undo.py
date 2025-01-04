import os
import shutil

path = input("Enter path: ")
subdirectories = os.listdir(path)

for subdir in subdirectories:
    subdir_path = os.path.join(path, subdir)


    if os.path.isdir(subdir_path):
        for file in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file)
            shutil.move(file_path, os.path.join(path, file))

        os.rmdir(subdir_path)
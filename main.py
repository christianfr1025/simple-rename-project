import os
import pathlib

def rename_files_folders(base_dir):
    for item in pathlib.Path(base_dir).iterdir():
        if not item.stem.startswith('.'):
            if item.is_file():
                if item.stem != item.stem.upper():
                    print(f"Renaming \n {item} to \n{os.path.join(item.parent, item.stem.upper() + item.suffix)} \n")
                    #item.rename(os.path.join(item.parent, item.stem.upper() + item.suffix))
            elif item.is_dir():
                if item.stem != item.stem.upper():
                    print(f"Renaming \n {item} to \n{os.path.join(item.parent, item.stem.upper())} \n")
                    #item.rename(os.path.join(item.parent, item.stem.upper()))
                rename_files_folders(item)


base_dir = "/Users/christianmendoza/Desktop/test-folder"
rename_files_folders(base_dir)
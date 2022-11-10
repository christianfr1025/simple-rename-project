import os
import pathlib

def rename_files_folders(base_dir):
    for item in pathlib.Path(base_dir).iterdir():
        print("Checking " + os.path.join(item.parent, item.name))
        if not item.stem.startswith('.'):
            if item.is_file():
                if item.stem != item.stem.upper():
                    print(f"Renaming \n '{item}' to \n'{os.path.join(item.parent, item.stem.upper() + item.suffix)}' \n")
                    item.rename(os.path.join(item.parent, item.stem.upper() + item.suffix))
            elif item.is_dir():
                if item.name != item.name.upper():
                    print(f"Renaming \n '{item}' to \n'{os.path.join(item.parent, item.name.upper())}' \n")
                    item.rename(os.path.join(item.parent, item.name.upper()))
                if item.name.find(".lr") == -1 and item.name.find(".LR") == -1:
                    rename_files_folders(item)


base_dir = "/Volumes/LI 2020"
rename_files_folders(base_dir)

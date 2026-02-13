import zipfile
import pathlib

def make_archive(filepaths, folderpath):
    base_dir = pathlib.Path(__file__).parent
    print(base_dir)
    destination_dir = base_dir / folderpath
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination_path = destination_dir / "compressed.zip"
    with zipfile.ZipFile(destination_path, "w") as archive:
        for filepath in filepaths:
            file_path = base_dir / filepath
            file_path = pathlib.Path(file_path)
            archive.write(file_path, arcname=file_path.name)



if __name__ == "__main__":
    print("in main")
    make_archive(filepaths=["bonus.py", "gui.py"], folderpath="dest")

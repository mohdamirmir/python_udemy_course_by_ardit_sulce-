import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    base_path="/Users/mamir/aamirs_learining_workspace/backend_python_developer/python_udemy_course_by_ardit_sulce/Day_18_App1_Build_a_Task_Manager_Desktop_GUI_Adding_Advanced_Features"
    extract_archive(f"{base_path}/compressed.zip", f"{base_path}/files")
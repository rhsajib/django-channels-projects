import os

def export_directory_structure(path, output_file):
    with open(output_file, "w") as file:
        for root, dirs, files in os.walk(path):
            root_dir = os.path.relpath(root, path)
            file.write(f"Directory: {root_dir}\n")
            for file_name in files:
                file_path = os.path.join(root_dir, file_name)
                file.write(f"  - {file_path}\n")

if __name__ == "__main__":
    project_directory = os.path.abspath(os.path.curdir)
    output_file = "directory_structure.txt"  # Change this to the desired output file name

    export_directory_structure(project_directory, output_file)
    print(f"Directory structure exported to {output_file}")

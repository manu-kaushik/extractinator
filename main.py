import os
import shutil
import zipfile

def create_new_folder_and_process_files(src_folder, output_folder):
    # Create the output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Walk through the src folder recursively
    for root, dirs, files in os.walk(src_folder):
        relative_path = os.path.relpath(root, src_folder)
        output_path = os.path.join(output_folder, relative_path)

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith('.zip'):
                # Unzip the contents of the zip file into a corresponding folder
                unzip_and_process(file_path, os.path.join(output_path, os.path.splitext(file)[0]))
            else:
                # Copy files directly
                shutil.copy(file_path, output_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            output_dir_path = os.path.join(output_folder, os.path.relpath(dir_path, src_folder))

            if not os.path.exists(output_dir_path):
                os.makedirs(output_dir_path)

def unzip_and_process(zip_path, extract_to):
    """Recursively unzips a zip file and processes nested zips."""
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Collect all extracted items and check for nested zips
    for root, _, files in os.walk(extract_to):
        for file in files:
            if file.endswith('.zip'):
                nested_zip_path = os.path.join(root, file)
                nested_extract_to = os.path.join(root, os.path.splitext(file)[0])
                
                unzip_and_process(nested_zip_path, nested_extract_to)  # Recursive call

                # Remove the nested zip file after extracting
                os.remove(nested_zip_path)

if __name__ == "__main__":
    # Define source and output folders
    src_folder = "src"
    output_folder = "output"

    # Process files and folders
    create_new_folder_and_process_files(src_folder, output_folder)

    print(f"All items from '{src_folder}' have been processed and placed in '{output_folder}'.")

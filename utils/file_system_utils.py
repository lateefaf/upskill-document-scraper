import os
import shutil

def clone_filesystem_structure(source_dir, target_dir):
    """
    Clone the folder structure from the source_directory to the destination_directory.

    :param source_dir: The source directory whose folder structure will be cloned.
    :param target_dir: The directory where the cloned folder structure will be placed.
    """
    for root, dirs, files in os.walk(source_dir):
        # Get the relative path of the current directory from the source_directory
        relative_path = os.path.relpath(root, source_dir)

        # Create the corresponding directory structure within the destination_directory
        destination_path = os.path.join(target_dir, relative_path)
        os.makedirs(destination_path, exist_ok=True)

        # Copy the files from the source directory to the destination directory
        for file in files:
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_path, file)

            shutil.copy(source_file_path, destination_file_path)
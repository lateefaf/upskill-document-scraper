import os

def clone_filesystem_structure(source_dir, destination_dir):
    """
    Clone the folder structure from the source_directory to the destination_directory.
    Only the directory structure is created; files are not copied.
    
    :param source_dir: The source directory whose folder structure will be cloned.
    :param destination_dir: The directory where the cloned folder structure will be created.
    """
    for root, dirs, files in os.walk(source_dir):
        # Get the relative path of the current directory from the source_directory
        relative_path = os.path.relpath(root, source_dir)

        # Create the corresponding directory structure within the destination_directory
        destination_path = os.path.join(destination_dir, relative_path)
        os.makedirs(destination_path, exist_ok=True)
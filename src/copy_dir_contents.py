import os

def copy_and_replace_directory_contents(src_dir, dest_dir):
    delete_dir_contents(dest_dir)
    copy_dir_contents(src_dir, dest_dir)

def delete_dir_contents(directory):
    if os.path.exists(directory):
        # Loop through all files and directories in the directory
        for file in os.listdir(directory):
            # If the file is a file, delete it
            if os.path.isfile(os.path.join(directory, file)):
                os.remove(os.path.join(directory, file))
            # If the file is a directory, delete its contents and then delete the directory
            else:
                delete_dir_contents(os.path.join(directory, file))
                os.rmdir(os.path.join(directory, file))

def copy_dir_contents(src_dir, dest_dir):
    # Loop through all files and directories in the source directory
    for file in os.listdir(src_dir):
        # If the file is a file, copy it
        if os.path.isfile(os.path.join(src_dir, file)):
            with open(os.path.join(src_dir, file), 'rb') as src_file:
                with open(os.path.join(dest_dir, file), 'wb') as dest_file:
                    dest_file.write(src_file.read())
        else:
            # If the file is a directory, create the directory in the destination directory and copy its contents
            create_dir_if_not_exists(os.path.join(dest_dir, file))
            copy_dir_contents(os.path.join(src_dir, file), os.path.join(dest_dir, file))

def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

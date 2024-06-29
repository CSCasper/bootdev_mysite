import os
import shutil

def copy_files_recursively(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for file in os.listdir(src):
        src_file = os.path.join(src, file)
        dest_file = os.path.join(dest, file)
        
        print('Copying', src_file, 'to', dest_file)
        if os.path.isdir(src_file):
            copy_files_recursively(src_file, dest_file)
        else:
            shutil.copy(src_file, dest_file)
            
def remove_all_files(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            remove_all_files(file_path)
        else:
            os.remove(file_path)
    os.rmdir(directory)

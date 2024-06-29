from copystatic import copy_files_recursively, remove_all_files

def main():
    remove_all_files('public')
    copy_files_recursively('static', 'public')
    
if __name__ == '__main__':
    main()
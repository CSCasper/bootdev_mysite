from copystatic import copy_files_recursively, remove_all_files
from generatecontent import  generate_pages_recursive

def main():
    remove_all_files('public')
    copy_files_recursively('static', 'public')
    generate_pages_recursive('public', 'template.html', 'public')
    
    
if __name__ == '__main__':
    main()
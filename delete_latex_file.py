import os, sys
from get_first_cell_value import *
from Version_finder import trimmed_file_name

def delete_file_and_folder(file_path):
    try:
        # Check if the file has a .tex extension
        if file_path.endswith(".tex") and not 'templates' in file_path.lower() and not 'template' in file_path.lower():
            # Adjusting the path to access the pdf file
            new_file_path = trimmed_file_name(file_path)
            new_file_path = 'Output/' + new_file_path + '.pdf'
            new_file_path = new_file_path.replace('_', ' ')
            
            # Use absolute path
            abs_file_path = os.path.abspath(new_file_path)

            # Delete the file
            os.remove(abs_file_path)

            # Get the directory of the file
            file_dir = os.path.dirname(abs_file_path)

            # Check if the directory is empty
            if not os.listdir(file_dir):
                # Delete the directory if it's empty
                os.rmdir(file_dir)
                print(f"Deleted file: {abs_file_path} and its empty folder.")
            else:
                print(f"Deleted file: {abs_file_path}. Folder not deleted as it's not empty.")
        else:
            print(f"Skipped non-.tex file: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def main():
    delete_file_and_folder(sys.argv[1])

if __name__ == "__main__":
    main()
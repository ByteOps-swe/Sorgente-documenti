import os, sys, re

def get_first_cell_value(filename):
    with open(filename, 'r') as file:
        data = file.read()
        match = re.findall(r'{}(.*?){}'.format("label{Git_Action_Version}", "&"), data, re.DOTALL)
        file.close()
        return match[0] if match else ''

def trimmed_file_name(file_path):
    new_file_path = "Documents/" + file_path
    filename_abs = os.path.join(os.getcwd(), new_file_path)
    version_number = get_first_cell_value(filename_abs)
    if "Verbale" in file_path or version_number == '':
        return file_path[:-4],  filename_abs, version_number
    else:
        return file_path[:-11], filename_abs, version_number

def delete_file(file_path):
    try:
        new_file_path = trimmed_file_name(file_path)
        new_file_path = new_file_path.replace('_', ' ') 
        file_name = os.path.basename(new_file_path)
        file_dir = os.path.dirname(new_file_path)
        file_dir = "Output/" + file_dir
        found_file = []
        file_dir = os.path.join(os.getcwd(), file_dir)
            
        for root, dirs, files in os.walk(file_dir):
            for file_names in files:
                if file_name in file_names:
                    found_file.append(os.path.join(root, file_names))
        if not found_file:
            print(file_path)
        else:
            for file in found_file:
                os.remove(file)
                if "Verbale" in file:
                    print(file_path)
    except FileNotFoundError:
        return


def rename_latex_file(filename , version_number):
    version_number = version_number.strip()
    new_filename = re.sub(r'_([^_]+)$', '', filename)
    if version_number:
        new_filename = new_filename + '_v' + version_number + '.tex'
        os.rename(filename, new_filename)
        print(new_filename)
    else:
        print("Valore non trovato o tabella non trovata.")

def main():
    if ".tex" not in sys.argv[1]:
        return None
    # if "Verbale" in sys.argv[1]:
    #     delete_file(sys.argv[1])
    else:
        file_path_delete, file_path, version_number = trimmed_file_name(sys.argv[1])
        delete_file(file_path_delete)
        rename_latex_file(file_path, version_number)
if __name__ == "__main__":
    main()
# The python code renames Latex files that should have the version number on the name of the file by getting it from the changelog table on the latex file.
# The python code is needed for deleting old pdf files that would have been compiled from the same github workflow that is used to call said script.
# If this is the first time the pdf has been created than the delete isn't needed
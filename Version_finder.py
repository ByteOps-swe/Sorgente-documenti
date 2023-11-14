import re, os, sys

def delete_file(file_path):
    try:
        new_file_path = file_path[:-11]
        new_file_path = new_file_path.replace('_', ' ') 
        file_name = os.path.basename(new_file_path)
        file_dir = os.path.dirname(new_file_path)
        file_dir = "Output/" + file_dir
        found_file = []
        found_file_rename = []
        # print("Here is the pwd: " + os.getcwd())
        file_dir = os.path.join(os.getcwd(), file_dir)
        # print("Here is the file_dir: " + file_dir)
        # print("Here is the arguemnts that has been given: " + file_path)
            
        for root, dirs, files in os.walk(file_dir):
            for file_names in files:
                if file_name in file_names:
                    found_file.append(os.path.join(root, file_names))
        for file in found_file:
            os.remove(file)
        # print(f"File '{found_file}' deleted successfully.")
    except FileNotFoundError:
        print("File non trovato")

def get_first_cell_value(filename):
    with open(filename, 'r') as file:
        data = file.read()
        match = re.findall(r'{}(.*?){}'.format("label{Git_Action_Version}", "&"), data, re.DOTALL)
        return match[0] if match else None

def rename_latex_file(filename):
    # print ("Rinomina")
    value = get_first_cell_value(filename)
    value = value.strip()
    new_filename = re.sub(r'_([^_]+)$', '', filename)
    # print ("Pyhton" + new_filename)
    if value:
        new_filename = new_filename + '_v' + value + '.tex'
        # print("Python pre")
        os.rename(filename, new_filename)
        # print("Python post")
        print(new_filename)
    else:
        # print('Valore non trovato o tabella non trovata.')

def main():
    if ".tex" not in sys.argv[1]:
        return None
    if "Verbale" in sys.argv[1]:
        return None
    else:
        delete_file(sys.argv[1])
        rename_latex_file(sys.argv[1])
if __name__ == "__main__":
    main()

import re

def get_first_cell_value(filename):
    with open(filename, 'r') as file:
        data = file.read()
        match = re.findall(r'{}(.*?){}'.format("label{Git_Action_Version}", "&"), data, re.DOTALL)
        return match[0] if match else None
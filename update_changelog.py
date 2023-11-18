import re

def add_version_row(table_content):
    # Find the last version number in the table
    match = re.search(r"\\label{Git_Action_Version}\s+(\d+\.\d+\.\d+)", table_content)
    
    if match:
        # Extract the last version number
        last_version = match.group(1)
        
        # Increment the last version
        version_parts = last_version.split('.')
        new_version = f"{int(version_parts[0])}.{int(version_parts[1])}.{int(version_parts[2]) + 1}"
    else:
        # If no version is found, start with 0.0.1
        new_version = "0.0.1"
    
    # Construct the new row
    new_row = f"\n    {new_version} \n\t\t      & <date> & <author> & <verifier> & <details> \\\\\n    \\hline\n"

    # Replace the placeholder with the new row
    updated_content = table_content.replace("\\label{Git_Action_Version}", f"\\label{{Git_Action_Version}}{new_row}   ")
    
    return updated_content

latex_table = """
\\section*{Registro delle modifiche}
\\begin{tabular}{|C{2.5cm}|C{2.5cm}|C{2.5cm}|C{2.5cm}|C{2.5cm}|}
    \\hline
    \\textbf{Versione} & \\textbf{Data}   & \\textbf{Autore}                         & \\textbf{Verificatore} & \\textbf{Dettaglio} \\\\
    \\hline \\hline
    \\label{Git_Action_Version} 0.2.0
                      & 06/11/2023      & Andrea Barutta,
    Nicola Preto      & Riccardo Smanio & Sezione Comunicazione,Gestione incontri                                              \\\\
    \\hline
    0.1.0
                      & 05/11/2023      & Davide Diotto
    Nicola Preto      & Riccardo Smanio & Sezione Documentazione,Introduzione                                                  \\\\
    \\hline
\\end{tabular}
"""

updated_latex_table = add_version_row(latex_table)
print(updated_latex_table)
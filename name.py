import re
import os

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)


def extract_name(file_name: str) -> str:
    """Extracts the President's name from the file name"""

    regex = r"Nomination_([A-Za-z ]+)([12]*)\.txt"

    name = None
    matched = re.search(regex, file_name)
    if(matched):
        name = matched.group(1)
    
    return name



for i in range (8) :
    if i=='Chirac':
        name["Chirac"] = Jacques Chirac
    if i=='Giscard d\'Estaing':
        name["Giscard d'Estaing"] = Jacques Chirac
    if i==Chirac:
        name["Chirac"] = Jacques Chirac
    if i==Chirac:
        name["Chirac"] = Jacques Chirac
    if i==Chirac:
        name["Chirac"] = Jacques Chirac
    if i==Chirac:
        name["Chirac"] = Jacques Chirac
    
import re
import os

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
folder = "./speeches"
file_names = list_of_files(folder, "txt")

def extract_name(file_name: str) -> str:
    """Extracts the President's name from the file name"""

    regex = r"Nomination_([A-Za-z ]+)([12]*)\.txt"

    name = None
    matched = re.search(regex, file_name)
    if(matched):
        name = matched.group(1)
    
    return name
names = []
for i in file_names:
    names.append(extract_name(i))


name = {}

for i in names:
    if i=='Chirac':
        name["Chirac"] = "Jacques"
    if i=='Giscard dEstaing':
        name["Giscard d'Estaing"] = "Valéry"
    if i=='Hollande':
        name["Hollande"] = 'François'
    if i=="Mitterrand":
        name["Mitterrand"] = 'François'
    if i=='Sarkozy':
        name["Sarkozy"] = 'Nicolas'
    if i=='Macron':
        name["Macron"] = 'Emmanuel'

print(name)
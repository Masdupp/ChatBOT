import re
import os

def list_of_files(directory, extension):
    '''Returns the names of the files in a directory
            Parameters :
            directory, extension 
        Returns:
            list_of_files : The list of all the files in the directory
    '''
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
folder = "./speeches"
file_names = list_of_files(folder, "txt")

def extract_name(file_name: str) -> str:
    """Extracts the President's name from the file names
        Parameters :
            file_name :The list of files
        Returns:
            name : list of all the names"""

    regex = r"Nomination_([A-Za-z ]+)([12]*)\.txt"

    name = None
    matched = re.search(regex, file_name)
    if(matched):
        name = matched.group(1)
    
    return name

names = []
for i in file_names:
    names.append(extract_name(i))


name_2 = {}

for i in names:
    if i=='Chirac':
        name_2["Chirac"] = "Jacques"
    if i=='Giscard dEstaing':
        name_2["Giscard dEstaing"] = "Valéry"
    if i=='Hollande':
        name_2["Hollande"] = 'François'
    if i=="Mitterrand":
        name_2["Mitterrand"] = 'François'
    if i=='Sarkozy':
        name_2["Sarkozy"] = 'Nicolas'
    if i=='Macron':
        name_2["Macron"] = 'Emmanuel'

print(name_2)
    
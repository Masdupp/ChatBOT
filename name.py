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
    if i in names:
        
    else:
        names.append(extract_name(i))


name = {"Jacques": " ", "Valéry": " ", "François": " ","François": " "," Nicolas": " ","Emmanuel" : " "}


print(names)
print(name)
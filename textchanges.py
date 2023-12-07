import os, shutil
import name

def modify_text_file_to_lowercase(file_path: str, new_folder_path: str, new_file_name: str) -> None:
    with open(file_path, 'r',encoding='utf8') as file:
        text = file.read().lower()
    new_file_path = os.path.join(new_folder_path, new_file_name)
    with open(new_file_path, 'w') as file:
        file.write(text)
text_to_modify = name.list_of_files(name.folder,"txt")
for j in text_to_modify:
    modify_text_file_to_lowercase(f"./speeches/{j}","./cleaned",j)


lowercase_letter = "abcdefghijklmnopqrstuvwxyzüéâäåçêëèïîìôöòûùÿáíóúñ"


def ponct_changes(file, directory):
    with open(file,'r') as f:
        text = f.read()
    res=" "
    for i in text:
        if i in lowercase_letter:
            res+=i
        else:
            res+= " "
    text=res



folder2="./cleaned"
files_names = name.list_of_files(folder2,"txt")

for i in files_names:
    ponct_changes(f"cleaned/{i}")

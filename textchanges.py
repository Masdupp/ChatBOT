import os
import name

def modify_text_file_to_lowercase(file_path: str, new_folder_path: str, new_file_name: str) -> None:
    with open(file_path, 'r') as file:
        text = file.read().lower()
    new_file_path = os.path.join(new_folder_path, new_file_name)
    with open(new_file_path, 'w') as file:
        file.write(text)
lowercase_letter = "abcdefghijklmnopqrstuvwxyzüéâäåçêëèïîìôöòûùÿáíóúñ"
def ponct_changes(file):
    f = open(file, "w")
    for i in f:
        if i not in lowercase_letter:
            i==""

folder2="./cleaned"
files_names=list_of_files(folder2,"txt")

for i in files_names:
    ponct_changes(i)
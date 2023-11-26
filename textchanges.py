import os
import name
import string
import re

def modify_text_file_to_lowercase(file_path: str, new_folder_path: str, new_file_name: str) -> None:
    with open(file_path, 'r') as file:
        text = file.read().lower()
    new_file_path = os.path.join(new_folder_path, new_file_name)
    with open(new_file_path, 'w') as file:
        file.write(text)
text_to_modify = name.list_of_files(name.folder,"txt")
for j in text_to_modify:
    modify_text_file_to_lowercase(f"./speeches/{j}","./cleaned",j)

lowercase_letter = "abcdefghijklmnopqrstuvwxyzüéàâäåçêëèïîìôöòûùÿáíóúñ123456789"
def ponct_changes(file_path: str):
    f = open(file_path, "r", encoding = 'utf-8')
    res = ""
    for i in f.read():
        if i in lowercase_letter:
            res += i
        else:
            res += " "
    with open(file_path, 'w') as file:
        file.write(res)


text_to_modifys = name.list_of_files(name.folder,"txt")
for j in text_to_modifys:
    ponct_changes(f"./cleaned/{j}")


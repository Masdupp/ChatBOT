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

#lowercase_letter = "abcdefghijklmnopqrstuvwxyzüéâäåçêëèïîìôöòûùÿáíóúñ"
#def ponct_changes(file):
#    f = open(file, "r")
#    res = ""
#    for i in f.read():
#        if i in lowercase_letter:
#            res += i
#        else:
#            res += " "

#folder2="./cleaned"
#files_names = name.list_of_files(folder2,"txt")



#for i in files_names:
#   print(i)
#    ponct_changes("speeches/" + i)


def remove_punctuation_and_special_cases(text):
    punctuation_except_special = re.sub(r'[^\w\s\'-]', '', text)
    
    cleaned_text = re.sub(r'\b\'\b', '', punctuation_except_special)
    cleaned_text = re.sub(r'\b-\b', ' ', cleaned_text)
    
    return cleaned_text

def clean_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
            content = file.read()
    cleaned_content = remove_punctuation_and_special_cases(content)
    with open(output_file_path, 'w') as file:
            file.write(cleaned_content)

clean_file(speeches/Nomination_Chirac1.txt,cleaned/Nomination_Chirac1.txt)
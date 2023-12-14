import os, shutil
import name
import string
import re
import math

def modify_text_file_to_lowercase(file_path: str, new_folder_path: str, new_file_name: str) -> None:
    with open(file_path, 'r',encoding='utf8') as file:
        text = file.read().lower()
    new_file_path = os.path.join(new_folder_path, new_file_name)
    with open(new_file_path, 'w') as file:
        file.write(text)
text_to_modify = name.list_of_files(name.folder,"txt")
for j in text_to_modify:
    modify_text_file_to_lowercase(f"./speeches/{j}","./cleaned",j)

lowercase_letter = "abcdefghijklmnopqrstuvwxyzüéàâäåçêëèïîìôöòûùÿáíóúñ1234567890"
def ponct_changes(file_path: str):
    f = open(file_path, "r", encoding = 'utf-8')
    res = ""
    for i in f.read():
        if i in lowercase_letter:
            res+=i
        else:
            res += " "
    with open(file_path, 'w') as file:
        file.write(res)


text_to_modifys = name.list_of_files(name.folder,"txt")
for j in text_to_modifys:
    ponct_changes(f"./cleaned/{j}")


def tf(string): #measures how often a word appears in a specific document
    dict = {}
    words = ""
    for i in string:
        if i == " " or i in ",;:!?./'-" or i == "\n" and words != "":
            if words in dict:
                dict[words] += 1
                words = ""
            elif words not in dict and words != "":
                dict[words] = 1
                words = ""
        if i not in ",;:!?./-' \n":
            words += i

    if words in dict:
        dict[words] += 1
    elif words not in dict and words != "":
        dict[words] = 1
    return dict

def idf(directory):  #measures the importance of a word in the entire corpus of documents
    files_names, types, dic = [], ".txt", {}
    word = ""
    directory = r"C:\Users\Tombi\Desktop\pychatbot-Thomas-Alexandre-int4-main" + "\\" + directory
    for namefile in os.listdir(directory):
        if namefile.endswith(types):
            with open(directory + "\\" + namefile, 'r', encoding = 'utf-8') as file:
                    for word in tf(file.read()):
                        if word in dic:
                            dic[word] += 1
                        if word not in dic:
                            dic[word] = 1
    for word in dic:
        dic[word] = math.log(8/dic[word])
    return dic

def tf_idf(directory): #score of a word in a given document is a numerical vector that reflects both the frequency of the word in that document and its relative importance in relation to the corpus as a whole
    matrix_td_idf = []
    ligne = []
    dict_idf = idf(directory)
    for filename in os.listdir(r"C:\Users\Tombi\Desktop\pychatbot-Thomas-Alexandre-int4-main" + "\\" + directory):
        if filename.endswith(".txt"):
            with open(r"C:\Users\Tombi\Desktop\pychatbot-Thomas-Alexandre-int4-main" + "\\" + directory + "\\" + filename, 'r', encoding = 'utf-8') as file:
                dict_tf = tf(file.read())
                for word in dict_idf:
                    if word in dict_tf:
                        ligne.append(dict_idf[word] * dict_tf[word])
                    if word not in dict_tf:
                        ligne.append(0)
            matrix_td_idf.append(ligne)
            ligne = []
    return matrix_td_idf
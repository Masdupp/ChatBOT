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
    directory = r"speeches" + "\\" + directory
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
    lign = []
    dict_idf = idf(directory)
    for filename in os.listdir(r"speeches" + "\\" + directory):
        if filename.endswith(".txt"):
            with open(r"speeches + ","\\" + directory + "\\" + filename, 'r', encoding = 'utf-8') as file:
                dict_tf = tf(file.read())
                for word in dict_idf:
                    if word in dict_tf:
                        lign.append(dict_idf[word] * dict_tf[word])
                    if word not in dict_tf:
                        lign.append(0)
            matrix_td_idf.append(lign)
            lign = []
    return matrix_td_idf

def least_important_words(directory):    #Display the list of least important words in the document corpus (TD-IDF=0)
    least_important_words_list = []
    dictionary = idf(directory)
    for word in dict:
        if dictionary[word] == 0:
            least_important_words_list.append(word)
    return least_important_words_list

def highest_TD_IDF_score(directory):       #Display the word with the highest TD-IDF score
    highest_TD_IDF_score_list = []
    dictionary = idf(directory)
    maximum = 0
    for word in dictionary:
        if dictionary[word] >= maximum:
            maximum = dictionary[word]
    for word in dictionary:
        if dictionary[word] == maximum:
            highest_TD_IDF_score_list.append(word)
    return highest_TD_IDF_score_list

def most_repeated_word_by_President(name): 
    dictionary_president= {}
    max = 0
    max_list = []
    for j in name.list_of_files("Cleaned", ".txt"):
        if name in j:
            with open(r"speeches" +  "\\" + j, 'r', encoding = 'utf-8') as file:
                dictionary = tf(file.read())
                for word in dictionary:
                    if word in dictionary_president:
                        dictionary_president[word] += dictionary[word]
                    elif word not in dictionary_president:
                        dictionary_president[word] = dictionary[word]
    for word in dictionary_president:
        if dictionary_president[word] > max:
            max = dictionary_president[word]
    for word in dictionary_president:
        if dictionary_president[word] == max:
            max_list.append(word)
    return max_list


def word_finder(word): #Find the president who said a word the most, how many time and other president who said the word
    dictionary_word_finder = {}
    maximum_mot, name_maximum = 0, ""
    list_name = name.extract_name(name.list_of_files("Speeches", "txt"))
    for filename in os.listdir(r"speeches"):
        if filename.endswith(".txt"):
            with open(r"speeches" +  "\\" + filename, 'r', encoding = 'utf-8') as file:
                dict = tf(file.read())
                for name in list_name:
                    if name in filename:
                        for word_dict in dict:
                            if word_dict == word:
                                if name in dictionary_word_finder:
                                    dictionary_word_finder[name] += dict[word_dict]
                                elif name not in dictionary_word_finder:
                                    dictionary_word_finder[name] = dict[word_dict]
    for name in dictionary_word_finder:
        if dictionary_word_finder[name] > maximum_mot:
            maximum_mot = dictionary_word_finder[name]
            name_maximum = name
    return name_maximum, dictionary_word_finder

def first_pronounced_word(word):    #return the name of the president that said a word first
    dictionary_word_finder = word_finder(word)
    list_name = ['Giscard dEstaing', 'Mitterrand', 'Chirac', 'Sarkozy', 'Hollande', 'Macron']
    minimum = len((list_name))
    for name in dictionary_word_finder:
        counter = 0
        for i in list_name:
            if name == i and minimum >= counter:
                minimum = counter
                name_minimum = i
            counter += 1
    return list_name[minimum], minimum

def word_by_all_president(word):     #return a word said by all the president
    dictionary = {}
    list_name = ['Giscard dEstaing', 'Mitterrand', 'Chirac', 'Sarkozy', 'Hollande', 'Macron']
    for filename in os.listdir(r"speeches\Cleaned"):
        if filename.endswith(".txt"):
            with open(r"speeches\Cleaned" + "\\" + filename, 'r', encoding = 'utf-8') as file:
                for name in list_name:
                    if name in filename:
                        for i in tf(file.read()):
                            if i == word:
                                if name in dictionary:
                                    dictionary[name] += 1
                                if name not in dictionary:
                                    dictionary[name] = 1
    if dictionary == {'Chirac': 1, 'Giscard dEstaing': 1, 'Hollande': 1, 'Macron': 1, 'Mitterrand': 2, 'Sarkozy': 1} or dictionary ==  {'Chirac': 2, 'Giscard dEstaing': 1, 'Hollande': 1, 'Macron': 1, 'Mitterrand': 1, 'Sarkozy': 1} or dictionary == {'Chirac': 1, 'Giscard dEstaing': 1, 'Hollande': 1, 'Macron': 1, 'Mitterrand': 1, 'Sarkozy': 1}:
        return 1
    if dictionary != {'Chirac': 1, 'Giscard dEstaing': 1, 'Hollande': 1, 'Macron': 1, 'Mitterrand': 2, 'Sarkozy': 1} or dictionary != {'Chirac': 2, 'Giscard dEstaing': 1, 'Hollande': 1, 'Macron': 1, 'Mitterrand': 1, 'Sarkozy': 1} or dictionary != {'Chirac': 1, 'Giscard dEstaing': 1, 'Hollande': 1, 'Macron': 1, 'Mitterrand': 1, 'Sarkozy': 1}:
        return 0
from name import *
from questions import *
from textchanges import *
import os

if __name__ == "__main__":
    directory = "cleaned/"
    tf_idf1 = tf_idf(directory)
    files_names = list_of_files("speeches/", ".txt")  # raw list of speeches names
    pres_dict = {}  # list of presidents names linked with their speeches filenames
    pres_dict = {k: [] for k in name_2}
    #print(pres_dict)
    for fn in file_names:
        n = extract_name(fn)
        pres_dict[n].append(fn)

    #print(pres_dict)
    print("Welcome to the Oscar's and Timothée's ChatBOT Analyst of French Presidents' Speeches !")
    print("Choose the option you want to discover !:")
    print("1. Display the names of the studied presidents")
    print("2. Display the least important words in all speeches")
    print("3. Display the matrix of the most important words in all speeches")
    print("4. Display the most used word in a specific speech")
    print("5. Display the presidents that have said a specific word")
    print("6. Display the first speeches to talk about a specific topic")
    print("7. Display the number of times a word is used in all speeches")
    print("8. Ask another question")
    print("9. Exit the program")
    choice = input("Please enter the number of the option you want to choose: ")
    while choice != "9":
        if choice == "1":
            print("Sure ! Here are the names of the presidents:")
            for name in name_2.keys():
                print(name)
        elif choice == "2":
            print("Of course ! Here are the least important words in all speeches:")
            lowest = least_important_words(directory)
            for i in lowest:
                print(i)
            print("These words are not important, meaning that their tf-idf score is 0!")
        elif choice == "3":
            print("Of course ! Here are the most important words in all speeches:")
            highest_TD_IDF_score(directory)
            print("These words are important because they are used in only one speech !")
        elif choice == "4":
            print("Certainly ! Here are the most used words in a specific speech:")
            print("Here are the names of the speeches:")
            for filename in list_of_files(directory, ".txt"):
                print(filename)
            filename = ""
            while filename not in list_of_files(directory, ".txt"):
                filename = input("Enter the name of the speech you want to analyze: ")
                if filename not in list_of_files(directory, ".txt"):
                    print("Try again, that's not a valid option.")
            print("There are the most used words in this speech", filename, ":")
            temp = most_repeated_word_by_President(filename)
            print(" ".join(temp))
        elif choice == "5":
            print("Sure! Here are the presidents who used a specific word:")
            word = input("Please enter the word you want to search: ")
            word = word.lower()
            print("Here are the presidents that used the word '", word, "':")
            temp, temp2 = [],[]
            for filename in list_of_files(directory,".txt"):
                with open(directory + filename, "r", encoding = 'utf-8') as f:
                    for line in f:
                        if word in line.lower():
                            temp.append(filename)
                            break
            for i, j in pres_dict.items():
                for k in j:
                    for cell in temp:
                        if k in cell and i not in temp2:
                            temp2.append(i)
            for cell in temp2:
                print(cell)
            if not temp2:
                print("Sorry, no president used this word.")            
        elif choice == "6":
            print("Let's do it ! Here is the first speech to talk about a specific topic:")
            word = input("Please enter the topic you want to search for: ")
            word = word.lower()
            print("Here is the president that was the first to talk about", word, ":")
            test, tmp = [], 0
            textchanges.first_pronounced_word(word)
            if not test:
                print("Sorry, no president have talked about this word.")
            else:
                print(test[0])        
            
        elif choice == "7":
            print("Yes good choice ! Here is the number of times a word is said in all speeches:")
            word = input("Please enter the word you're looking for: ")
            word = word.lower()
            print("There is the number of times the word", word, "is said in all of the speeches :", end=" ")
            tmp = " "
            nb_time=[0]
            for filename in list_of_files("Cleaned","txt"):
                tmp = tf(filename)
                nb_time.append(tmp)

            if nb_time[0]==0:
                print()
                print("Sorry, no president have talked about this word, maybe the next president will.")
            else:
                print(tmp[word])
        #elif choice == "8":
            #question = input("Yes I can do this ! Enter a question and I'll answer from the speeches !")
            #question = words_from_words(question)
            #tmp = ""
            #for filename in list_of_files("Cleaned","txt"):
        else:
            print("Sorry, this is not a valid option.")
        choice = input("Please enter the number of the option you want to choose: ")
    print("Thank you for using the Oscar's and Timothée's ChatBOT Analyst of French Presidents' Speeches !")
def maj_changes(directory, extension):












lowercase_letter = "abcdefghijklmnopqrstuvwxyzüéâäåçêëèïîìôöòûùÿáíóúñ"
def ponct_changes(file):
    f = open(file, "w")
    for i in f:
        if i not in lowercase_letter:
            i==""

ponct_changes(/speeches/Nomination_Chirac1.txt)
ponct_changes(/speeches/Nomination_Chirac2.txt)
ponct_changes(/speeches/Nomination_Giscard dEstaing.txt)
ponct_changes(/speeches/Nomination_Hollande.txt)
ponct_changes(/speeches/Nomination_Macron.txt)
ponct_changes(/speeches/Nomination_Mitterrand1.txt)
ponct_changes(/speeches/Nomination_Mitterrand2.txt))
ponct_changes(/speeches/Nomination_Sarkozy.txt)
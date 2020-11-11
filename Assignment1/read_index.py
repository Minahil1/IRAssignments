import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

Dict = {}
file = open("termids.txt", "r+")
List = file.read()
Lines = word_tokenize(List)

Runti = len(Lines)
Runti = int(Runti / 2)
count = 0
for i in range(Runti):
    Dict[Lines[count + 1]] = Lines[count]
    count += 2
file.close()

file = open("term_index.txt", "r+")
List = file.readlines()

term = input("Enter a term here:")
print("Listing for term: " + term + "\n")
term = ps.stem(term)

value = int(Dict[term])
print("TERMID:" + str(value) + "\n")
value -= 1
Line = word_tokenize(List[value])
print("Number of Documents carrying term:" + str(Line[2]) + "\n")
print("Term frequency in corpus:" + str(Line[1]))

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

DocDict = {}
file = open("docids.txt", "r+")
List = file.read()
Lines = word_tokenize(List)

Runti = len(Lines)
Runti = int(Runti / 2)
count = 0
for i in range(Runti):
    DocDict[Lines[count + 1]] = Lines[count]
    count += 2
file.close()

file = open("output.txt", "r+")
List = file.read()
Lines = word_tokenize(List)

Runti = len(Lines)
Runti = int(Runti / 2)
count = 0
OutDict = {}
for i in range(Runti):
    w = Lines[count + 1]
    if w in DocDict:
        w2 = Lines[count]
        w2 = int(w2)
        if w2 in OutDict:
            docid = int(DocDict[w])
            OutDict[w2].add(docid)

        else:
            docid = int(DocDict[w])
            OutDict[w2] = set()
            OutDict[w2].add(docid)

    count += 2
file.close()


file = open("term_index.txt", "r+")
List = file.readlines()

file = open("my_output.txt", "r+")
QueryList = file.readlines()
file.close()

myOutDict = {}
DictKey = ""
for i in QueryList:
    count = 0
    QueryLine = word_tokenize(i)
    for term in QueryLine:
        if count == 0:
            DictKey = int(term)
            myOutDict[DictKey] = set()
        else:
            myOutDict[DictKey].add(int(term))
        count += 1

print("printing output" + "\n")
print(myOutDict[850])
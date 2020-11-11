import os
import nltk
import math

nltk.download('punkt')  # this is for running this first time
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# read stopwords
f = open("stopwords.txt", "r")
stopwords = f.read()
f.close()

# take input
path = input("enter path: \n")

# list of filenames
files = []
ps = PorterStemmer()
# root, directories, files
for root, directories, allfiles in os.walk(path):
    for file in allfiles:
        files.append(os.path.join(root, file))

Dict = {}
count = 0
# reset docids.txt
open('docids.txt', 'w').close()
for f in files:
    count2 = 1  # term id count
    count += 1  # document id count
    print(count)  # helps to check when the loop will exit the loop, debugging purposes
    file = open(f, encoding='utf-8')
    file2 = open("docids.txt", "a+")
    write = f.replace(path + '\\', '')
    file2.write(str(count) + "\t" + write + "\n")
    data = file.read()

    words = word_tokenize(data)  # using nltk word tokenizeer
    for w in words:
        w = w.lower()  # convert to lowercase
        if w not in stopwords:  # remove stopwords
            if w.isalpha():  # remove punctuations and numbers
                w = ps.stem(w)  # stem words
                if w in Dict:  # increment count of term in the whole corpus
                    Dict[w][0] += 1
                    Dict[w].append([count, count2])  # add document-termid pair
                else:
                    Dict[w] = [1, 1]  # term not in dictionary, add list first index for term frequency in corpus,
                    # second for frequency fo documents
                    # the term appears in
                    Dict[w].append([count, count2])  # append document-termid pair
                count2 += 1

Dict = dict(sorted(Dict.items()))  # sort terms alphabetically, Python 3.6 function iirc

print("Out of the reading loop")
count2 = 1
Inverted_Index = {}
count = 1
# reset termindex, termids.txt
open('term_index.txt', 'w').close()
open('termids.txt', 'w').close()
stopFinder = []
WordsFrequency = []
LogFrequency = []

for w in Dict:

    fileterm = open("termids.txt", "a+")
    fileterm.write(str(count) + "\t" + w + "\n")
    Inverted_Index[count] = [1, 1]
    Inverted_Index[count][0] = Dict[w][0]
    stopFinder.append([Dict[w][0], w, count])
    WordsFrequency.append([Dict[w][0], w])
    LogFrequency.append([math.log10(Dict[w][0]), w])
    count2 = 0
    newList = []
    uniqueDocuments = set()

    for i in Dict[w]:
        if count2 > 1:
            newList.append(i)
            uniqueDocuments.add(i[0])
        count2 += 1
    newList.sort()

    sizeofUniqueDocuments = len(uniqueDocuments)

    if sizeofUniqueDocuments > 0:
        Inverted_Index[count][1] = sizeofUniqueDocuments
    sizeofList = len(newList) - 1

    for i in newList:
        if sizeofList >= 1:
            newList[sizeofList][0] -= newList[sizeofList - 1][0]
        if newList[sizeofList][0] == 0:
            newList[sizeofList][1] -= newList[sizeofList - 1][1]
        sizeofList -= 1

    Inverted_Index[count].append(newList)
    count += 1

# this checks top 30 stop words, stop words were deleted manually
stopFinder.sort()
print(stopFinder[-30:])

for i in Inverted_Index:

    fileindex = open("term_index.txt", "a")
    fileindex.write(str(i) + " ")
    spacecount = 0
    for j in Inverted_Index[i]:
        x = str(j).replace(', ', ',')  # all the replace rules are to format this according to the assignment document
        x = str(x).replace(',[', ', ')
        x = str(x).replace('],', '')
        x = str(x).replace('[', '')
        x = str(x).replace(']', '')
        if spacecount < 2:
            fileindex.write(x + " ")
        else:
            fileindex.write(x)
        spacecount += 1
    fileindex.write("\n")

# This is to print the graph in Task 4
WordsFrequency.sort()
WordsFrequency.reverse()

open("wordfrequency.csv", "w").close()
f = open("wordfrequency.csv", "a")
for i in WordsFrequency:
    f.write(str(i[0]) + ",")
    f.write(i[1])
    f.write("\n")
f.close()

LogFrequency.sort()
LogFrequency.reverse()

open("Logfrequency.csv", "w").close()
f = open("Logfrequency.csv", "a")
for i in LogFrequency:
    f.write(str(i[0]) + ",")
    f.write(i[1])
    f.write("\n")
f.close()
print(LogFrequency)

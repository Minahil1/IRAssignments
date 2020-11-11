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

print(Dict)

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

file = open("term_index.txt", "r+")
List = file.readlines()
file.close()

f = open("stopwords.txt", "r")
stopwords = f.read()
stopwords = word_tokenize(stopwords)
f.close()

file = open("query.txt", "r+")
QueryList = file.readlines()
file.close()

open('my_output.txt', 'w').close()
file = open("my_output.txt", "a+")

UnionMerger = set()

for i in QueryList:
    count = 0
    Querytfdf = []
    lenUnion = len(UnionMerger)
    print("length Union")
    print(lenUnion)

    unioncount = 0
    if lenUnion > 0:
        for j in UnionMerger:
            file.write(str(j))
            if unioncount < lenUnion - 1:
                file.write("\t")
            else:
                print("wrote a whole set for a query")
                file.write("\n")
            unioncount += 1

    UnionMerger = set()
    QueryLine = word_tokenize(i)
    for term in QueryLine:
        if count == 0:
            print(term)
            file.write(term + "\t")
            queryid = int(term)
        else:
            # print("Listing for term: " + term + "\n")
            term = term.lower()
            if term not in stopwords and term.isalpha():
                term = ps.stem(term)

                value = int(Dict[term])
                # print(value)
                value -= 1
                Line = word_tokenize(List[value])
                # print(Line)
                count = 3

                Querytfdf = []
                # print("entered loop")
                for i in range(len(Line)):
                    if i > 3:
                        Line[count] = str(Line[count]).replace(',', ' ')
                        Line[count] = str(Line[count]).replace('[', '')
                        Line[count] = str(Line[count]).replace(']', '')
                        Line[count] = str(Line[count]).replace('\'', '')
                        Line[count] = word_tokenize(Line[count])
                        if Line[count][0] != '' and Line[count][1] != '':
                            value1 = int(Line[count][0])
                            value2 = int(Line[count][1])
                            Querytfdf.append([value1, value2])
                    if count < i:
                        count += 1
                # print("exited loop")
                # print(Querytfdf)
                Set = set()
                sizeofList = 0
                for i in Querytfdf:
                    if sizeofList >= 1:
                        if Querytfdf[sizeofList][0] == 0:
                            Querytfdf[sizeofList][1] += Querytfdf[sizeofList - 1][1]
                        Querytfdf[sizeofList][0] += Querytfdf[sizeofList - 1][0]
                        Set.add(Querytfdf[sizeofList][0])
                    sizeofList += 1
                UnionMerger = UnionMerger.union(Set)

        count += 1
file.close()

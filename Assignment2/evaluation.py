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

print(Lines)
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

print("printing output")
print(myOutDict)

open('performance.txt', 'w').close()
file = open("performance.txt", "a+")

accuracyList = []
precisionList = []
recallList = []

for i in myOutDict:
    print("printing i")
    print(i)
    queryid = i
    file.write(str(i) + "\t")
    UnionMerger = myOutDict[queryid]
    print(UnionMerger)
    RelevantDocs = OutDict[queryid]

    print("RelevantDocs")
    print(RelevantDocs)
    print("\n")

    print("UnionMerger")
    print(UnionMerger)
    print("\n")

    truePositive = UnionMerger.intersection(RelevantDocs)
    falseNegative = RelevantDocs.difference(UnionMerger)
    falsePositive = UnionMerger.difference(RelevantDocs)

    print("truePositive")
    print(truePositive)
    print("\n")
    print("falsePositive")
    print(falsePositive)
    print("\n")
    print("falseNegative")
    print(falseNegative)
    print("\n")

    truePositiveCount = len(truePositive)
    falseNegativeCount = len(falseNegative)
    falsePositiveCount = len(falsePositive)
    trueNegativeCount = 6377 + truePositiveCount - falseNegativeCount - falsePositiveCount

    Accuracy = (truePositiveCount + trueNegativeCount) / (
            truePositiveCount + trueNegativeCount + falsePositiveCount + falseNegativeCount)

    Recall = truePositiveCount / (truePositiveCount + falseNegativeCount)

    Precision = truePositiveCount / (truePositiveCount + falsePositiveCount)

    print(Accuracy)
    accuracyList.append(Accuracy)
    file.write(str(Accuracy) + "\t")
    print(Precision)
    precisionList.append(Precision)
    file.write(str(Precision) + "\t")
    print(Recall)
    recallList.append(Recall)
    file.write(str(Recall) + "\n")
file.close()

lengthofaccList = len(accuracyList)
lengthofpreList = len(precisionList)
lengthofrecList = len(recallList)

accuracySum = 0
precisionSum = 0
recallSum = 0
count = 0
for i in accuracyList:
    accuracySum += accuracyList[count]
    precisionSum += precisionList[count]
    recallSum += recallList[count]

print("Average accuracy:")
print(accuracySum/lengthofaccList)
print("\n")
print("Average precision:")
print(precisionSum/lengthofpreList)
print("\n")
print("Average recall:")
print(recallSum/lengthofrecList)
print("\n")
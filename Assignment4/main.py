import os
from decimal import Decimal


def returnfilenames(path):
    files = []
    for root, directories, allfiles in os.walk(path):
        for file in allfiles:
            files.append(os.path.join(root, file))
    return files


def getWordList(path):
    count = 1
    WordList = []
    files = returnfilenames(path)
    for f in files:
        count += 1  # document id count
        print(count)  # helps to check when the loop will exit the loop, debugging purposes
        file = open(f)
        data = file.read()

        words = data.split()
        for w in words:
            w = w.lower()  # convert to lowercase
            if w.isalpha():  # remove punctuations and numbers
                WordList.append(w)
    return WordList, count


def train_native_bayes():
    count = 1
    WordList, count = getWordList("train/ham")
    count2 = 1
    WordList2, count2 = getWordList("train/spam")
    WordlList3 = WordList+WordList2
    print(WordlList3)

    N = count + count2

    Dict = {}

    for w in WordList:
        if w.isalpha():  # remove punctuations and numbers
            if w in Dict:  # increment count of term in the whole corpus
                Dict[w] += 1
            else:
                Dict[w] = 1

    Dict2 = {}

    for w in WordList2:
        if w.isalpha():  # remove punctuations and numbers
            if w in Dict2:  # increment count of term in the whole corpus
                Dict2[w] += 1
            else:
                Dict2[w] = 1

    V=set(WordlList3)
    V=len(V)

    hamcount=len(WordList)
    spamcount=len(WordList2)

    ProbDict1 = {}
    for i in Dict:
        ProbDict1[i] = (Dict[i] + 1) / (hamcount + V)

    ProbDict2 = {}
    for i in Dict2:
        ProbDict2[i] = (Dict2[i] + 1) / (spamcount + V)

    dictCount1 = len(ProbDict1)
    dictCount2 = len(ProbDict2)
    N = dictCount1 + dictCount2
    priorc1 = count / N
    priorc2 = count2 / N

    return priorc1, ProbDict1, WordList, priorc2, ProbDict2, WordList2, V, hamcount, spamcount


priorc1, ProbDict1, WordList, priorc2, ProbDict2, WordList2, V, hamcount, spamcount = train_native_bayes()


# print(ProbDict1)
# print(ProbDict2)

def test_native_bayes(priorc1, ProbDict1, WordList, priorc2, ProbDict2, WordList2, N,hamcount, spamcount, path):
    files = returnfilenames(path)
    print(path)
    filecount = 0
    hamcount = 0
    spamcount = 0
    for f in files:
        file = open(f, encoding="utf8", errors='ignore')
        write = f.replace(path + '\\', '')
        data = file.read()

        words = data.split()
        probham = Decimal(priorc1)
        probspam = Decimal(priorc2)
        for w in words:
            w=w.lower()
            if w.isalpha():
                if w in ProbDict1:
                    probham *= Decimal(ProbDict1[w])
                elif w not in ProbDict1:
                    probham *= Decimal(1 / (hamcount +N))

        for w in words:
            w = w.lower()
            if w.isalpha():
                if w in ProbDict2:
                    probspam *= Decimal(ProbDict2[w])
                elif w not in ProbDict2:
                    probspam *= Decimal(1 / (spamcount + N))
        if probham > probspam:
            hamcount += 1
        else:
            spamcount += 1
        filecount += 1

    return hamcount, spamcount


truenegative, falsepositive = test_native_bayes(priorc1, ProbDict1, WordList, priorc2, ProbDict2, WordList2, V,hamcount, spamcount,
                                                "test/ham")
falsenegative, truepositive = test_native_bayes(priorc1, ProbDict1, WordList, priorc2, ProbDict2, WordList2, V,hamcount, spamcount,
                                                "test/spam")

print(truenegative)
print(falsepositive)
print(falsenegative)
print(truepositive)

precision=truepositive/(truepositive+falsepositive)
recall=truepositive/(truepositive+falsenegative)
F1score=(2*precision*recall)/(precision+recall)
accuracy=(truepositive+truenegative)/(truepositive+truenegative+falsenegative+falsepositive)

print("precision is:" + str(precision))
print("recall is:" + str(recall))
print("F1score is:" + str(F1score))
print("accuracy is:" + str(accuracy))
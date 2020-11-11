f = open("jang.txt", "r", encoding='utf-8')
Lines = f.read()

Lines = Lines.replace('<', '').replace('s', '').replace('>', '').replace('/', '')
# print(Lines)


Lines = Lines.split()
Dict = {}
print(Lines)
f.close()

f = open("errors.txt", "r", encoding='utf-8')
Errors = f.read()
Errors = Errors.replace('<', '').replace('s', '').replace('>', '').replace('/', '')
Errors = Errors.split()
f.close()

f = open("nonerrors.txt", "r", encoding='utf-8')
nonErrors = f.read()
nonErrors = nonErrors.replace('<', '').replace('s', '').replace('>', '').replace('/', '')
nonErrors = nonErrors.split()
f.close()

f = open("wordlist.txt", "r", encoding='utf-8')
WordList = f.read()
WordList = WordList.replace('<', '').replace('s', '').replace('>', '').replace('/', '')
WordList = WordList.split()
WordList = set(WordList)
f.close()

# Lines = ['omens','minahil', 'bad', 'bad']

for word in Lines:
    if word in Dict.keys():
        Dict[word] += 1
    else:
        Dict[word] = 1

count = len(Lines)
print(Dict)

for word in Dict:
    Dict[word] = Dict[word] / count

print(Dict)

error=set(Errors)
nonErrors=set(nonErrors)

nonErrors=nonErrors.difference(error)

i = 0
prevword = ""
Dict2 = {}
for word in Lines:
    if i == 0:
        prevword = word
    if i > 0:
        Dict2[prevword + " " + word] = Dict[prevword] * Dict[word]
        prevword = word
    i += 1

print(Dict2)




def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'ابپتٹثجچحخدڈذرڑزژسشصضطظعغفقکگلمنوہیے'

    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

Errorlist = []
ErrorDict= {}
Lines=set(Lines)

count=0
for error in Errors:
    if error not in WordList:
        resultedit1 = edits1(error)

        resultantset = set()

        for oneedit in resultedit1:
            # print(edits1(oneedit))
            resultantset = resultantset.union(edits1(oneedit))

        candidates = resultantset.intersection(WordList)
        LL = []
        for i in candidates:
            string1=Errors[count-1] +" " + i
            string2=i + " " + Errors[count+1]
            score=0

            if i in Dict.keys():
                score+=5*Dict[i]

            if string1 in Dict2.keys() and string2 in Dict2.keys():
                score +=2*(Dict2[string1]* Dict2[string2])
            LL.append([score, i])
            LL.sort(key=lambda x: x[0], reverse=True)
            if len(LL) > 10:
                LL.pop(10)


        if len(LL) > 0:
            setcand = set()

            #print(LL)

            for j in range(len(LL)):
                setcand.add(LL[j][1])
            #print(setcand)
            print(setcand)
            ErrorDict[error]=LL

        Errorlist.append(error)
    count+=1

f = open("errors.txt", "r", encoding='utf-8')
Errors = f.read()
Errors = Errors.replace('<', '').replace('s', '').replace('>', '').replace('/', '')
Errors = Errors.split()
f.close()

f = open("nonerrors.txt", "r", encoding='utf-8')
nonErrors = f.read()
nonErrors = nonErrors.replace('<', '').replace('s', '').replace('>', '').replace('/', '')
nonErrors = nonErrors.split()
f.close()

print(len(ErrorDict))

count=0
f = open("errorcandidates.csv", "a", encoding='utf-8')
for i in Errors:
    if i!=nonErrors[count]:
        LL=ErrorDict[i]
        f.write("error:" + i+": ")

        setcand=set()
        for j in range(len(LL)):
            setcand.add(LL[j][1])

        f.write("candidates: ")

        for j in setcand:
            f.write(str(j)+" ")
        if nonErrors[count] in setcand:
            f.write("status: found " +str(nonErrors[count]) +" ")
        else:
            f.write("status: not found" + " ")
        f.write("\n")
    count+=1
f.close()

import re


def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list


# Driver code

list = ['geeks', '3for', '4geeks', '202', 'go', 'washington', 'such', 'geeks', 'haad', 'loves', 'himself', 'haad', 'is',
        'special', 'one']
print(remove(list))

f = open("stopwords.txt", "r")
stopwords = (f.read())
# print(stopwords)

t = "D:\lldocs\GX236-11-14453828"
print(t.replace('D:\lldocs' + '\\', ''))

Dictionary = {}

freq = {}
List=[]
count = 1
for item in list:
    ListObject=[]
    if item in freq:
        freq[item][0] += 1
        freq[item][1] += 1
        freq[item].append(count)
        List.append(ListObject)

    else:
        freq[item] = [1,1]
        freq[item].append(count)
        List.append(ListObject)

    count += 1

for key, value in freq.items():
    print(key, value)

newList=[]
newList.sort()
print(newList)


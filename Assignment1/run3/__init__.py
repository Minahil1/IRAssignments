dictionary = dict(C1=[10, 20, 30], C2=[20, 30, 40])

for x in range(len(dictionary["C1"])):
    dictionary["C1"][x] += 10

#print(dictionary)

List =[[432,43], [456,33], [456,41] ]
List.sort()
#print(List)
count=0
count=len(List)-1
for i in List:
    if count >= 1:
        #print(List[count][0])
        List[count][0] -= List[count-1][0]
    count -= 1




Dict=[[462,43], [427,33] ,[427,21], [427,5],[426,0]]
print(Dict)
Dict.sort()
print(Dict)

sizeofList = len(Dict) - 1
for i in Dict:
    if sizeofList >= 1:
        Dict[sizeofList][0] -= Dict[sizeofList - 1][0]
    if Dict[sizeofList][0] == 0:
        Dict[sizeofList][1] -= Dict[sizeofList - 1][1]
    sizeofList -= 1

print(Dict)
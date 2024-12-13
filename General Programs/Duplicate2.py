# Que. Remove duplicates from a list without using set.
List = ['Element' , 2 , 4 , 'e' , 'o' , 4 , 'Element' , 2 , 4 , 'e' , 'o' , 4 , 2 , 4 , 'e' , 'o' ,  4 , 'Element' , 2 , 4 , 'e' , 'o' ]
uniqueList = []

for i in range(len(List)) :
    if List[i] not in uniqueList :
        uniqueList.append(List[i])

print(uniqueList)
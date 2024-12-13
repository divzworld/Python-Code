# Que. Remove duplicates from a list without using set.
List = ['Element' , 2 , 4 , 'e' , 'o' , 4 , 'Element' , 2 , 4 , 'e' , 'o' , 4 ]

i = 0 
while i <= len(List) :
    j = i + 1
    while j < len(List) :
        if List[i] == List[j] :
            List.remove(List[j])
        else :
            j += 1
    i += 1

print(List)
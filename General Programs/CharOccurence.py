# Que.  Write a program to count the occurrences of each element in a list.
List = ['Element' , 2 , 4 , 'e' , 'o' , 4 , 'Element' , 2 , 4 , 'e' , 'o' , 4 , 2 , 4 , 'e' , 'o' ,  4 , 'Element' , 2 , 4 , 'e' , 'o' ]
unique_List = []

for item in List :
    if item not in unique_List :
        unique_List.append(item)
print(unique_List)

count = 0
for i in unique_List :
    count = 0
    for j in List : 
        if i == j :
            count += 1
    print(f"{i} Occurence is : {count}")
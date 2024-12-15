# Que. Create a dictionary from two lists : one for keys and one for values.

List1 = [ 1 , 2  ,  3 , 4 , 5 , 6 ]
List2 = ['Divya' , 'Sakshi' , 'Pooja' , 'Shravani' , 'Vaibhavi' , 'Rutuja']
dict = {}

for i in range(len(List1)) :
    dict[List1[i]] = List2[i]

print(dict)
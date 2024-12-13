# Que. Write a program to merge two sorted lists into one sorted list.
List1 = [ 2, 4, 56 , 9 ]
List2 = [ 56 , 43  , 67 , 12 ]

List1 = sorted(List1)
List2 = sorted(List2) # Remember sorted() not helps when list contains both int and string 

mergedList = List1 + List2

print(sorted(mergedList))
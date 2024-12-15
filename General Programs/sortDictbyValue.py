# Que. Write a program to sort a dictionary by its values.

dict1 = {5: 'Vaibhavi', 3: 'Pooja', 4: 'Shravani',  6: 'Rutuja' , 1: 'Divya', 2: 'Sakshi'}
sortedDict = {}

sortedDict = dict(sorted(dict1.items(), key = lambda item : item[1]))

print(sortedDict)
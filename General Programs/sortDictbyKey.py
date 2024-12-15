# Que. Write a program to sort a dictionary by its keys.
dict = {5: 'Vaibhavi', 3: 'Pooja', 4: 'Shravani',  6: 'Rutuja' , 1: 'Divya', 2: 'Sakshi'}
sortedDict = {}

sortedDict = {key : dict[key] for key in sorted(dict)}
print(sortedDict)
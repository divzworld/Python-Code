# Que. Merge two dictionaries and print the result.
dict1 = {1: 'Divya', 3: 'Pooja', 6: 'Rutuja', 2: 'Sakshi', 4: 'Shravani', 5: 'Vaibhavi'}
dict2 =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mergeDict = (dict1 | dict2) # merge operator -- > ( | )
print(mergeDict)
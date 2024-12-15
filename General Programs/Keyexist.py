# Que. Write a program to check if a given key exists in a dictionary.
dict = {1: 'Divya', 3: 'Pooja', 6: 'Rutuja', 2: 'Sakshi', 4: 'Shravani', 5: 'Vaibhavi', 'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

choice = input(" Enter the key that you are looking for : ")

if choice.isdigit() : # becoz input() is always str and that will not accept numeric values
    choice = int(choice)

if choice in dict :
    print(dict[choice], "Is available in Dictionary")
else :
    print(f"{dict[choice]} is not avaiable in Dictionary")
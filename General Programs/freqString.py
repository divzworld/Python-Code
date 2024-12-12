# Que. Count the frequency of each character in a string.

inputString = input(" Enter the string : ")
uniqueString = set(inputString)
for ch in uniqueString :
    print(f"{ch }: {inputString.count(ch)}")
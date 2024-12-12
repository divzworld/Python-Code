# Que. Replace all occurrences of a specific word in a string with another word.
inputString = input(" Enter the sentence : ").strip().lower()

oldWord = input(" Enter the word that you want to replace : ").lower()
newWord = input(" Enter the word that will be replaced by : ").lower()

tempList = list(inputString.split())
print(tempList)

for i in range(len(tempList)) :
    if tempList[i] == oldWord :
        tempList[i] = newWord

print(" New Sentence after replacement : ", " ".join(tempList))
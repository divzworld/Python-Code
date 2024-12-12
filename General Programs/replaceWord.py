# Que. Replace all occurrences of a specific word in a string with another word.
inputString = input(" Enter the sentence : ").strip().lower()
print("Sentence :", inputString)

oldWord = input(" Enter the word that you want to replace : ").lower()
newWord = input(" Enter the word that will be replaced by : ").lower()

print(" String after replacing word : ",inputString.replace(oldWord,newWord))

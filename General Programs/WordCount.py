# Que. Write a program to count the number of words in a sentence.

sentence = input(" Enter the sentence : ").strip()
while "  " in sentence :
    sentence = sentence.replace("  "," ")
print(sentence)
SpaceCount = 0
for _ in sentence :
    if " " in sentence :
        SpaceCount += 1


WordCount = SpaceCount + 1 # (+1) beacause here I'm calculating spaces between two words
print(f" In sentence there are {WordCount} words . ")

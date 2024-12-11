# Que. Write a program to count the number of words in a sentence.
import sys
sentence = input(" Enter the sentence : ").strip()

# After striping check words are present or only white spaces are there !
if not sentence :
    print(" No words !")
    sys.exit()

while "  " in sentence :
    sentence = sentence.replace("  "," ")
print(sentence)
SpaceCount = 0
for char in sentence :
    if char == " ":
        SpaceCount += 1

if SpaceCount > 0 :
    WordCount = SpaceCount + 1 # (+1) beacause here I'm calculating spaces between two words
    print(f" In sentence there are {WordCount} words . ")
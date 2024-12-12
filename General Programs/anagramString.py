# Que.  Write a program to check if two strings are anagrams.
"""
An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

Examples:
"listen" → "silent"
"evil" → "vile"
"rail safety" → "fairy tales" (ignoring spaces and case sensitivity)
"""
stringOne = input(" Enter the string : ").replace(" ","").lower()
stringTwo = input(" Enter the string : ").replace(" ","").lower()
List1 = list(stringOne)
List2 = list(stringTwo)

print(sorted(List1))
print(sorted(List2))

if len(stringOne) == len(stringTwo) :
    if sorted(List1) == sorted(List2) :    
        print(f" '{stringOne}' and '{stringTwo}' those Strings are anagrams ")
    else :
        print(f" '{stringOne}' and '{stringTwo}' those Strings are not anagrams ")

else :
    print(f" '{stringOne}' and '{stringTwo}' those Strings are not anagrams ")
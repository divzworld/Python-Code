# Que. Write a program to check whether a character is a vowel or a consonant.
while True :
    character = input(" Enter the Single Alphabet : ").strip().lower()
    if len(character) > 1 :
        print(" Please enter only one character ! ")
    elif character.isdigit() == True :
        print(" Please enter only one alphabet e.g. 'A' , 'a' etc. ! ")
    else :
        break

vowel = ['a','e','i','o','u']
for char in character :
    if char in vowel :
        print(f"{character} Is a vowel ")
    else :
        print(f"{character} Is a consonant ")
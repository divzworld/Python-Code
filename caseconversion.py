""" Que. Take input string(mixed up uppercase and loercase) from user and in that if uppercase letters are more than lowercase then at the end
whole string may print in uppercase and vice versa ."""


def caseCheck(inputStr) :
    UpperCase = inputStr.upper()
    LowerCase = inputStr.lower()
    UpperCaseCount = 0
    LowerCaseCount = 0
    for char in inputStr :
        if char in UpperCase :
            UpperCaseCount += 1
        elif char in LowerCase :
            LowerCaseCount += 1

    if UpperCaseCount < LowerCaseCount :
        print(inputStr.lower())
    elif LowerCaseCount < UpperCaseCount :
        print(inputStr.upper())  




caseCheck(input(" Enter String only : ").strip())
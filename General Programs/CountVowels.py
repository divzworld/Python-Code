# Que. Write a function to count the number of vowels in a string.
def VowelCount(StringParam) :
    count = 0
    String = StringParam
    for char in String.lower() :
        if char in 'aeiou' :
            count += 1
    return count


StringParam = input("Enter the string :")
result = VowelCount(StringParam)
print(f" In '{StringParam}' there are {result} Vowels ")
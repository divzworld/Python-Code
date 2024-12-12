# Que. Write a program to reverse a string without using slicing.
inputStr = input(" Enter the String : ").strip()
tempList = []

for ch in inputStr :
    tempList.append(ch)

print(tempList)
reverseList = [] # Temporary list to save list items in reverse order
# Inserting items in a list
for item in tempList :
    reverseList.insert(0,item)

#print(reverseList)
reverseString = ("".join(reverseList))
print(f"{inputStr} in reverse form is : ",reverseString)
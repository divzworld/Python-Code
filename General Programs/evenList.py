# Que. Write a function that takes a list and returns a new list with only even numbers

def evenList(listParam) :
    list = listParam
    evenList = []
    for i in range(len(list)) :
        if list[i] % 2 == 0 :
            evenList.append(list[i])

    return evenList


listParam = []
try :
    count = int(input(" Enter how many numbers you want to add : "))
    print(" Insert elements : ")
    while count > 0 :
        listParam.append(int(input()))
        count -= 1
except ValueError as e :
    print(" Error : ",e)

evenList(listParam)
# Printing output
print(f" Original List : {listParam} Extracted Even List : {evenList(listParam)}")
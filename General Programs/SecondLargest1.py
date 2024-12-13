# Que. Write a program to find the second largest number in a list.

num = int(input(" Enter how much items you want to insert in a list : "))
List = []
while num > 0 :
    try :
        List.append(int(input(" Enter the number : ")))
        num -= 1
    except ValueError as e :
        print(" Error : " , e)
print(" List : ",List)
for i in range (len(List)) :
    for j in range (len(List)-i-1) :
        if List[j] > List[j+1] :
            List[j] , List[j+1] = List[j+1] , List[j]

print(" List after sorting : ",List)
print(" Second Largest From List Is : ",List[-2])   # -2 is an index number which means second last
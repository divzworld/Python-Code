# Que. Write a function to find the maximum and minimum of a list of numbers.

def MinMax(ListParam) :
    List = ListParam
    for i in range(len(List)) :
        for j in range(len(List)-i-1) :
            if List[j] > List[j+1] :
                #Swapping
                List[j] , List[j+1] =  List[j+1] , List[j]
            
    return List[1] , List[-1]


List = []
try :
    count = int(input(" Enter how many numbers you want to add : "))
    print(" Insert elements : ")
    while count > 0 :
        List.append(int(input()))
        count -= 1
except ValueError as e :
    print(" Error : ",e)
print("Your List Is : ",List)
print(f" From Given List {List} Minimum And MAximum Number are : ",MinMax(List))
# Que. Check if a number is an Armstrong number.
while True :
    try :
        num = int(input(" Enter the number : "))
        break
    except ValueError as e :
        print("Error :" , e)
List = []
temp = num
while temp > 0 :
    digit = temp % 10
    List.append(digit)
    temp //= 10

print(" List : ",List)
sumOfDigit = 0
for i in List :
    temp = i ** 3
    sumOfDigit += temp
    temp = 0

#print(sumOfDigit)
if sumOfDigit == num :
    print(f"{num} is an armstrong number")
else :
    print(f"{num} is not an armstrong number")
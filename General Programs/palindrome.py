# Que. . Write a function to check if a number is a palindrome.

while True :
    try :
        num = int(input(" Enter the number : "))
        if type(num) == int :
            break
    except ValueError as e :
        print(" Error :",e)

temp = num
tempList = []
CrossCheck = 0

while num > 0 :
    temp2 = num % 10
    tempList.append(temp2)
    num //= 10

CrossCheck = int("".join(map(str,tempList)))
if temp == CrossCheck :
    print(f"{temp} Is a Palindrome Number ")
else :
    print(f"{temp} Is not a Palindrome Number ")
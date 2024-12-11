# Que. . Write a function to check if a number is a palindrome.

def palindrome(num) :
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



while True :
    try :
        num = int(input(" Enter the number : "))
        if type(num) == int :
            palindrome(num)
            break
    except ValueError as e :
        print(" Error :",e)


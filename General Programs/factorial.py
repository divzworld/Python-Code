# Que. Write a program to calculate the factorial of a number using a loop

while True :
    try :
        num = int(input(" Enter the number : "))
        if num > 0 :
            break
        else :
            pass

    except ValueError as e :
        print("Error :",e)

fact = 1

for i in range (1, num+1) :
    fact = fact * i

print(f"The factorial of {num} is : {fact}")
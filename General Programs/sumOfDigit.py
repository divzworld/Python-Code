# Que. Write a program to find the sum of digits of a number.
while True :
    try :
        num = int(input(" Enter the number : "))
        if type(num) == int :
            break
    except ValueError as e :
        print(" Error :",e)

temp = num
sum = 0
while num > 0 :
    digit = num % 10
    sum += digit
    num //= 10


print(f" Sum of Digit {temp} Is :{sum}")
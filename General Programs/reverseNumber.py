# Que. Write a program to reverse a number using a loop.

while True :
    try :
        num = int(input(" Enter the number : "))
        if type(num) == int :
            break
    except ValueError as e :
        print(" Error :",e)

temp = []
while num > 0 :
    digit = num % 10 # for getting last digit
    temp.append(digit)
    num //= 10  # for reducing last digit from num otherwise loop will run infinite times 

print(temp)

for i in temp :
    print(i,end="")
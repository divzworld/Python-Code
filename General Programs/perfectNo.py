# Que. Write a program to check if a number is a perfect number.
num = int(input(" Enter the number : "))
sumOfDigit = 0

for i in range (1, num) :
    if num % i == 0 :
        sumOfDigit += i
    else :
        continue

if num == sumOfDigit :
    print(f"{num} is a perfect number !")
else :
    print(f"{num} is not a perfect number !")
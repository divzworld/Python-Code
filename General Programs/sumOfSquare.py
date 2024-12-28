# Que. Write a program to find the sum of squares of the first N natural numbers.

num = int(input(" Enter N for natural numbers : "))
numm = num
sumOfSquare = 0

while num > 0 :
    temp = num ** 2
    sumOfSquare += temp
    num -= 1

print(f"Sum of squares of the first {numm} natural numbers : {sumOfSquare}")
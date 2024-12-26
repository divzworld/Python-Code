# Que.  Write a program to generate the Fibonacci sequence up to a given number of terms.

maxRange = int(input(" Enter the number for max range : "))
num = 0
fib1 = num
fib2 = 1
print(fib1,"\n")
while num < maxRange+1 :
    print(fib2,"\n")
    num = fib1
    fib1 = fib2
    fib2 = num + fib1
    num += 1
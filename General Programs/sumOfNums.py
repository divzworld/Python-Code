# Que. Write a program to print the sum of all numbers from 1 to a given number.
sumOfNum = 0
try :
    num = int(input( " Enter the end point of Range : "))
    # for loop
    for i in range ( 1, num + 1) :
        sumOfNum  += i 
    # printing statement for printing sum of numbers
    print(f"Sum of 1 to {num} is : {sumOfNum}")

except ValueError as e :
    print("Error :" , e )


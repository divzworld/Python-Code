# Que. Write a program to print the multiplication table of a number entered by the user

try :
    # Enter the number for printing the multiplication table
    num = int(input(" Enter the number : "))
    for i in range ( 1 , 11 ):
        print(f"{num} x {i} = {num*i}")

except ValueError as e :
    print(" Error : ", e)
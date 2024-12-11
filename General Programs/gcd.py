# Que. Create a function to calculate the GCD (Greatest Common Divisor) of two numbers

def gcd(a , b) :
    # Variables
    num1 = a
    num2 = b

    # Empty List Creation
    List1 = []
    List2 = []

    # For loop to check divisors
    for i in range ( 1 , num1+1 ):
        if num1 % i == 0 :
            List1.append(i)

    for i in range ( 1 , num2+1 ):
        if num2 % i == 0 :
            List2.append(i)

    # nested for loop to check common divisor
    temp = []
    for i in List1 :
        for j in List2 :
            if i in List2 :
                temp.append(i)

    GCD = temp[-1]
    return GCD


num1 , num2 = int(input(" Enter the number 1 : ")) , int(input(" Enter the number 2 : "))
print(f" The GCD og {num1} , {num2} iS : ",gcd(num1,num2))
# Que. Write a program to convert a decimal number to binary.
num = float(input(" Enter the decimal number : "))
num = round(num)
list = [] # purpose - remainder will written in reverse order so we are using list
numm = num 

while num > 0 :
    remainder = num % 2 
    num = num // 2 # reduces num by dividing 2 and discarding fractional part
    #print(remainder)
    list.append(remainder)

list = list[::-1]
binaryConversion = "".join(map(str,list))
print(f"The Binary conversion of {numm} is : {binaryConversion}")
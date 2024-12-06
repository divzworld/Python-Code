"""
E = mc^2
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""

mass = int(input(" Enter the Mass in Kg : "))
E = mass *(300000000 **2)
print("Energy in joules : ",E)

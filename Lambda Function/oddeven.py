# Que.02 Write a lambda that checks if a number is even.
"""
checkNumber = lambda num : num % 2 == 0 

num = int(input(" Enter the number : "))
print(checkNumber(num))

"""
checkNumber = lambda num : "Even" if num % 2 == 0 else "Odd"

num = int(input(" What's num ?"))
print(checkNumber(num))
# Que.  Write a program to swap two numbers without using a temporary variable.

num1 = 10
num2 = 20

# Before swapping
print(f"Before swapping Those two numbers are num1 :{num1} , num2 :{num2}")

# Code for swap the numbers
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"After swapping Those two numbers are num1 :{num1} , num2 :{num2}")
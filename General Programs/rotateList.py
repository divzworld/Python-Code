# Que. Write a program to rotate a list by a given number of steps.
"""
The task is to write a Python program that rotates the elements of a list by a given number of steps. Rotation means shifting elements in the list to the left or right while wrapping the overflowed elements around to the other end.

Key Points:
Right Rotation: Shifts elements to the right, and the last elements wrap around to the front.
Left Rotation: Shifts elements to the left, and the first elements wrap around to the back.
Example:
Suppose you have a list:

python
Copy code
nums = [1, 2, 3, 4, 5]
Right Rotation by 2 steps:

After 1 step: [5, 1, 2, 3, 4]
After 2 steps: [4, 5, 1, 2, 3]
Result: [4, 5, 1, 2, 3]

Left Rotation by 2 steps:

After 1 step: [2, 3, 4, 5, 1]
After 2 steps: [3, 4, 5, 1, 2]
Result: [3, 4, 5, 1, 2]

Input:
A list of numbers.
The number of steps to rotate (positive integer).
Direction of rotation (optional, default to right).
Output:
A new list after rotation.
"""
List = [2, 4, 9, 56, 12, 43, 56, 67]
rightRotation = list(List)
leftRotation = list(List)

num = int(input(" Enter the number for steps : "))
steps = len(List)

# In case the numbers are more than length of list so for reducing unnecessary shift
if num > steps :
    num = num % steps

choice = int(input(" Select which rotation you want : "))

match(choice) :
    case 1 :
        print(" Right rotation !")
    case 2 :
        print(" Left rotation !")
    case _:
        print(" Invalid choice !")

if choice == 1 :
    while num > 0 :
        rightRotation = rightRotation[: 1] + rightRotation[1 :]
        num -= 1
    print(rightRotation)
elif choice == 2 :
    while num > 0 :
        leftRotation = leftRotation[1 :] + leftRotation[: 1]
        num -= 1
    print(leftRotation)
else :
    print(" Rotation not performing due to invalid choice by user!")
# Create a class `Student` with a constructor using **Encapsulation**. Add a method to show grade based on marks.

import random
class Student :
    def __init__ (self , marks : int) :
        self.__marks = None
        self.getMarks = marks

    # Getter Method
    @property
    def getMarks (self) -> int :
        return self.__marks
        
    # Setter Method
    @getMarks.setter
    def getMarks (self, marks) -> None : # none cause not returning any value
        if marks >= 0 and marks <= 100 :
            self.__marks = marks
        else :
            print(" Invalid marks ! So assigning random marks ")
            self.__marks = random.randint(1,100)

    def gradeDisplay (self) -> str :
        if self.__marks >= 70 :
            return "A+"
        elif self.__marks >= 60 :
            return "A"
        elif self.__marks >= 50 :
            return "B+"
        elif self.__marks >= 35 :
            return "B"
        else :
            return "F"
        
    def __str__(self) :
        return (f"Your Marks : {self.__marks} , Your grade is {self.gradeDisplay()}")
        


obj = Student(86)
obj.getMarks = 84
print(obj)

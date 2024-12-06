# Que. Write a program to check if a number is positive, negative, or zero And Take a number as input and check if it is even or odd.

class NumberType :
    def getinput( self ) : 
        try :
            self.num = int(input(" Enter the number : "))
        except :
            print(" Please enter valid input in numeric form ! ")
            self.getinput()
        self.checkNumber()
        self.oddEven()
    
    def checkNumber( self ) :
        if self.num < 0 :
            return "Negative Number"
        elif self.num > 0 :
            return "Positive Number"
        else :
            return "It's a Zero"
        
    def oddEven( self ) :
        if self.num % 2 == 0 :
            return "Even Number"
        else :
            return "Odd Number"
        
# Object creation for class
obj = NumberType()
obj.getinput()
print(f"The Number {obj.num} is {obj.checkNumber()} as well as {obj.oddEven()}")
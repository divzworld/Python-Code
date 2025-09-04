# Use **Constructor Overloading**: Create a class `Calculator` that supports multiple operations using default parameters.
class Calculator :
    def __init__ (self, num1=20, num2=5) :
        self.num1 = num1
        self.num2 = num2
        # Operations
    def addition(self) -> float :
        return self.num1 + self.num2
    
    def subtraction(self) -> float :
        return self.num1 - self.num2
    
    def multiplication(self) -> float :
        return self.num1 * self.num2
    
    def division(self) -> float :
        if self.num2 != 0 :
            return self.num1 / self.num2
        else :
            raise ZeroDivisionError("Error : Zero Division Error")

    def result(self, option) :
        #self.option = option # No need it b'coz we are using it in only method not in entire class
        if option == 1 :
            return f" Addition : {self.addition()}"
        elif option == 2 :
            return f" Subtraction : {self.subtraction()}"
        elif option == 3 :
            return f" Multiplication : {self.multiplication()}"
        elif option == 4 :
            return f" Division : {self.division()}"
        else :
            return " Invalid option ! Please choose in range 1 to 4"

    
     

cal = Calculator()
print(cal.result(3))

cal1 = Calculator(4)
print(cal1.result(2))

cal2 = Calculator(num2 = 15)
print(cal2.result(2))
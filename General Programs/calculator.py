# Que. Implement a basic calculator with options for addition, subtraction, multiplication, and division.
class calculator :
    def addition(self,param1,param2) :
        self.num1 = param1
        self.num2 = param2
        print(f"Addition :{self.num1 + self.num2}")

    def substraction(self,param1,param2) :
        self.num1 = param1
        self.num2 = param2
        print(f"Substraction :{self.num1 - self.num2}")

    def multiplication(self,param1,param2) :
        self.num1 = param1
        self.num2 = param2
        print(f"Multiplication :{self.num1 * self.num2}")

    def division(self,param1,param2) :
        self.num1 = param1
        self.num2 = param2
        print(f"Division :{self.num1 / self.num2}")


obj = calculator()

num1 = int(input(" Enter the number : "))
num2 = int(input(" Enter the number : "))

choice = int(input(" Enter the choice 1 , 2 , 3 or 4 : "))
match choice :
    case 1 :
        obj.addition(num1,num2)
    case 2 :
        obj.substraction(num1,num2)
    case 3 :
        obj.multiplication(num1,num2)
    case 4 :
        obj.division(num1,num2)
    case _ :
        print(" Invalid Choice ! Please make a choice in between 1 to 4 only ")
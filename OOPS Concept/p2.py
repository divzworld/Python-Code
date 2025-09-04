#  Define a class `Rectangle` that uses **Abstraction** to hide the internal calculation of area and perimeter.
# ABC - Abstract base class

from abc import ABC , abstractmethod
class RectangleAbs(ABC) : # abstract class
    @abstractmethod
    def area(self) :
        pass

    @abstractmethod
    def perimeter(self) :
        pass

class RectangleCal(RectangleAbs) : # concrete class
    def __init__(self, length : float, breadth : float) :
        self.length = length
        self.breadth = breadth

    def area(self) -> float :
        return self.length * self.breadth
    
    def perimeter(self) -> float :
        return 2*(self.length + self.breadth)
    
    def display(self) -> None :
        print(f" Area of Rectangle : {self.area()} \n Perimeter of Rectangle : {self.perimeter()}")


obj = RectangleCal(10,20)
obj.display()
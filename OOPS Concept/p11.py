# Use **Abstract Base Classes**: Create an abstract class `Shape` and implement `area()` method in `Square` and `Triangle`.
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC) : 
    @abstractmethod
    def area(self) :
        pass

class Square(Shape) :
    def __init__(self, side) :
        self.side = side

    def area(self)-> float :
        # side * side
        return self.side ** 2

class Triangle(Shape) :
    def __init__(self, base, height) :
        self.base = base
        self.height = height

    def area(self)-> float :
        #(base * height) / 2
        return (self.base*self.height)/2

    
sq = Square(5)
square = sq.area()
print(f"Area of Square : {square}")

tr = Triangle(4,6.2)
triangle = tr.area()
print(f"Area of Triangle : {triangle}")
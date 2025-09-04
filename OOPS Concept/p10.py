# Create a class `Circle` using **Class Variables** like `pi` and methods to compute area and circumference.
class Circle :
    pi = 3.14 # Class Variables

    def __init__(self, radius, circumference) :
        self.radius = radius
        self.circumf = circumference

    def areaOfCircle(self) -> float :
        # area = pi*r^2
        return Circle.pi * (self.radius**2)

    def areaByCircumference(self) -> float: # area using circumference
        # area = C^2 / (4*pi)
        return ((self.circumf ** 2) / (4*Circle.pi))
    
obj = Circle(4,3.5)
result1 = obj.areaOfCircle()
print(f" Area of Circle using Radius : {result1}")

result2 = obj.areaByCircumference()
print(f" Area of Circle using Circumference : {result2}")
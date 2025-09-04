# Use **Operator Overloading** to define a class `ComplexNumber` and override the `+` and `-` operators.
class CompleaxNumber :
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self, other) :      # self is obj1, other is obj2
        return CompleaxNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self,other) :       # self is obj1, other is obj2
        return CompleaxNumber(self.real - other.real, self.imag - other.imag)
    
    def __str__(self) :
        return f"{self.real} + {self.imag}i"
    


obj1 = CompleaxNumber(4,8)
obj2 = CompleaxNumber(6,7)
#  c1 + c2  # Internally: c1.__add__(c2) same for other
print(obj1 + obj2)
print(obj1 - obj2)
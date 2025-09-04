#  Use **Polymorphism** by creating a base class `Animal` and derived classes `Dog` and `Cat` that override `make_sound()` method.
from abc import ABC , abstractmethod

class Animal(ABC) :
    @abstractmethod
    def make_sound(self) -> None :
        pass

class Dog(Animal) :
    def make_sound(self) -> None :
        print(" Bhaw Bhaw ")

class Cat(Animal) :
    def make_sound(self) -> None :
        print(" Meow Meow ")


"""dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()"""

# Another way 
for animal in [Cat(), Dog()] :
    animal.make_sound()
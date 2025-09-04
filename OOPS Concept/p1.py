#  Create a class `Person` using **Encapsulation** with private attributes `name` and `age`. Add a method to display them.

class Person :
    def __init__(self, name, age) :
        self.__name = name #Private attributes
        self.__age = age #Private attributes

    def DisplayDetails(self) :
        print(f"Details of Persons are : \nName : {self.__name} \nAge : {self.__age}")

    # Getter Method

    def get_name(self) :
        return self.__name
    
    def get_age(self) :
        return self.__age
    
    # Setter Method

    def set_name(self, name) :
        self.__name = name

    def set_age(self, age) :
        if age > 0 :
            self.__age = age
        else :
            print("Age Should be positive !!")
   


obj = Person("Divya", 23)
obj.DisplayDetails()

# Getter method using for accessing private attribute
print(f"Getter methods :  Name - {obj.get_name()} \n Age - {obj.get_age()}")

# Setter method for setting values for private attributes
obj.set_name("Vedang")
obj.set_age(4)

print(f"Getter methods :  Name - {obj.get_name()} \n Age - {obj.get_age()}") # Testing updated values using getter method
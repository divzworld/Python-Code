# Create a class `Car` with attributes `brand`, `model`. Use **Class and Instance Variables** to differentiate between all cars 
# and specific ones

class Car :
    # Class attributes/variables
    wheels = 4
    engine = "V8"

    def __init__( self, brand, model, year, fuel) :
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel

    def __str__(self) :
        return f"Brand :{self.brand} , Model :{self.model} , Year :{self.year} , Wheels :{Car.wheels} , Engine :{Car.engine} , fuel :{self.fuel},"

obj1 = Car("Rolls-Royce", "Phantom", 2023, "Petrol")
print(obj1)

obj2 = Car("BMW", "X5", 2022, "Diesel")
print(obj2)

obj3 = Car("Mercedes-Benz", "S-Class", 2024, "Diesel")
print(obj3)
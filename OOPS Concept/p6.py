# Use **Inheritance**: Create a base class `Employee` and a derived class `Manager` with additional attributes and methods
class Employee :
    def __init__(self, emp_name, emp_address, age) :
        self.emp_name = emp_name
        self.emp_address = emp_address
        self.age = age

class Manager(Employee) :
    def __init__(self, emp_name, emp_address, age, salary) :
        super().__init__(emp_name, emp_address, age)
        self.salary = salary

    def __str__(self) :
        return f"Name :{self.emp_name}\t Address :{self.emp_address}\t Age :{self.age}\t Salary :{self.salary}"
 
obj = Manager("Rudra","Pune",26,50000)

print(obj)
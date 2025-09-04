# Demonstrate **Multiple Inheritance** using `Father`, `Mother`, and a subclass `Child` that inherits features from both.
class Father :
    def __init__(self,fname):
        self.fname = fname

class Mother :
    def __init__(self,mname):
        self.mname = mname

class Child(Father,Mother) :
    def __init__(self,myname,mname,fname,surname):
        Father.__init__(self,fname) 
        Mother.__init__(self,mname)
        self.myname = myname
        self.surname = surname
        

    def __str__(self):
        return f" Student Name :{self.myname}\n Mother Name :{self.mname}\n Father Name :{self.fname}\n Surname :{self.surname}"

child = Child("Divya","Sadhana","Jayakar","Yadav")
print(child)
#  Design a **Mini OOP System** for school: Classes `Student`, `Teacher`, `Course`, showing **Abstraction**, **Inheritance**, and **Polymorphism** together.
from abc import ABC, abstractmethod

class School : # Abstract Class
    def __init__(self,teacher_id,teacher_name,courses) :
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.course_name = courses

    @abstractmethod
    def get_details(self) :
        pass

# ----------------- Student Class ----------------- ----------------- ----------------- 
class Student(ABC) :
    def __init__(self,stud_name,stud_id) :
        self.stud_name = stud_name
        self.stud_id = stud_id
        self.enrolled_course = None
    
    def get_details(self) :
        self.enrolled_course = input(""" ------ Enter your choice for cource enrollment ------
                                     01. Data Science \n02.AI/ML \n03.Cyber Security \n04.DevOps : """)
    
    def __str__(self) :
        return f"Student Name : {self.stud_name} \n Student Id : {self.stud_id} \n Enrolled Course : {self.enrolled_course}"
    
# ----------------- Teacher Class ----------------- ----------------- ----------------- 
class Teacher :
    def __init__(self, teacher_id, subject) :
        self.teacher_id = teacher_id
        self.subject = subject
        self.assign_course = None

    def get_details(self) :
        self.assign_course = input(" Enter Assigned Course : ")

    def __str__(self) :
        return f"Teacher Id : {self.teacher_id}\n Subject : {self.subject} \n Assigned Course : {self.assign_course}"

# ----------------- Course Class ----------------- ----------------- ----------------- 
class Course(School) :
    def __init__(self,teacher_id,teacher_name,course_name) :
        super().__init__(teacher_id,teacher_name,course_name)
        self.course_name = course_name
        self.students = []
        self.teachers = []

    def add_student(self, student: Student) :
        self.students.append(student)

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def get_details(self):
        return f"Course: {self.course_name}, Total Students: {len(self.students)}, Teachers: {len(self.teachers)}"

    def __str__(self):
        result = f"\n📘 Course: {self.course_name}\n"
        result += "\n👨‍🏫 Teachers:\n"
        for teacher in self.teachers:
            result += f" - {teacher}\n"
        result += "\n👩‍🎓 Students:\n"
        for student in self.students:
            result += f" - {student}\n"
        return result

# ---------- Main Execution ----------
if __name__ == "__main__":
    # Create a Course
    course = Course(101, "Dr. Sharma", "AI/ML")

    # Add Students
    s1 = Student("Divya", "S001")
    s1.get_details()
    course.add_student(s1)

    s2 = Student("Manu", "S002")
    s2.get_details()
    course.add_student(s2)

    # Add Teachers
    t1 = Teacher("Anjali", "T001")
    t1.get_details()
    course.add_teacher(t1)

    # Show Course Summary
    print("\n--- Course Summary ---")
    print(course.get_details())

    # Show full details
    print("\n--- Full Details ---")
    print(course)
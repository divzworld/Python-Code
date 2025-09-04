# Q.11. You have a list of students with (name, marks). Get only those who scored above 40.
# students = [("Rahul", 35), ("Sneha", 90), ("Amit", 50)]

students = [("Rahul", 35), ("Sneha", 90), ("Amit", 50)]
result = list(filter(lambda x: x[1] > 40 , students))
print(result)
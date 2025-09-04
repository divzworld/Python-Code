# Que.12 Sort the same list by marks in descending order.
# students = [("Rahul", 35), ("Sneha", 90), ("Amit", 50)]

students = [("Rahul", 35), ("Sneha", 90), ("Amit", 50)]
result = sorted(students, key = lambda x : x[1] , reverse = True)
print(result)
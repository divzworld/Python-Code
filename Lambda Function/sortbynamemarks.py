# Que.21 Sort students by last name and then by marks (if last name is same).

data = [
     {"name": "Divya Yadav", "marks": 90},
    {"name": "Rudra Yadav", "marks": 95},
    {"name": "Abhi Desai", "marks": 91}
]

result = sorted(data, key = lambda x : ( x ["name"].split()[-1], -x ["marks"]))

print(result)

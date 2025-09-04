# Que.17  Use lambda + filter() to get employees who joined after 2020.
# employees = [
# {"name": "Divya", "join_year": 2019},
# {"name": "Neha", "join_year": 2021},
# ]

employees = [
{"name": "Divya", "join_year": 2019},
{"name": "Neha", "join_year": 2021},
]
print(type(employees))

result = list(filter(lambda x : x["join_year"] > 2020 , employees))
print(result)
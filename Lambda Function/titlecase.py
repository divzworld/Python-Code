# Que.24  Use lambda with map() to title-case a list of messy names.
#mnames = ['manU', 'DIVYA', 'rahUl']
# Output → ['Manu', 'Divya', 'Rahul']

names = ['manU', 'DIVYA', 'rahUl']
result = list(map(lambda x : x.title() , names))

print(result)
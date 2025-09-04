# Que.04 Use filter() + lambda to get only numbers > 3 from a list
number = [3,6,1,2,6,4,9,12,10,-3]

result = filter(lambda x: x > 3 , number)

print(list(result))
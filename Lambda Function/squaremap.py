# Que.03 Create a list of numbers [1,2,3,4,5] and use map() with lambda to square them.

ListOfNum = [1,2,3,4,5]
square = map(lambda x : x ** 2, ListOfNum)

print(list(square))
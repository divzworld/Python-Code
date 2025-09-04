# Que.06 Sort a list of tuples based on the second value using lambda.
# data = [(1, 5), (3, 1), (4, 8)]
# Expected → [(3, 1), (1, 5), (4, 8)] // Output
data = [(1, 5), (3, 1), (4, 8)]
result = sorted(data, key= lambda x:x[1])
print(result)
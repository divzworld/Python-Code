# Que.08 Sort dictionary items by value using lambda.
# d = {'a': 3, 'b': 1, 'c': 2}
# Expected → [('b', 1), ('c', 2), ('a', 3)]

"""
dictionary.items()

Converts dictionary into a list of tuples:
[('a', 3), ('b', 1), ('c', 2)]
Each tuple is (key, value).
"""

dictionary = {'a': 3, 'b': 1, 'c': 2} 
sorted_dict = sorted( dictionary.items() , key = lambda x : x[1])



print(sorted_dict)
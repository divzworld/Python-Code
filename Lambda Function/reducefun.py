# Que.15  Use reduce() + lambda to multiply all numbers in a list.
from functools import reduce

data = [1,2,3,4,5,6]
result = reduce (lambda x,y : x * y , data) 
print(result)

"""
“Why use reduce() instead of a loop?”

Answer like a pro:

"reduce() expresses the intent clearly: we want to reduce a list to a single value using a binary operation. 
It's concise and avoids manually managing accumulators."
"""
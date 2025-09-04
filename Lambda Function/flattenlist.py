# Que. 18  Given a nested list, flatten it using lambda + reduce().
# data = [[1, 2], [3, 4], [5]]
# Expected → [1, 2, 3, 4, 5]

from functools import reduce

data =  [[1, 2], [3, 4], [5]]
flatten_list = reduce( lambda x,y : x + y , data ) # Concat

print(flatten_list)

"""
🧠 INTERVIEW TAKEAWAY

If they ask why + works here, answer:

"Because list concatenation with + merges two lists into one, and reduce() keeps applying that until only one final list is left."
✅ Step-by-step:

reduce() starts with first two elements:

x = [1, 2], y = [3, 4] → x + y = [1, 2, 3, 4]

Then takes result [1, 2, 3, 4] as new x and next element y = [5] → [1, 2, 3, 4] + [5] = [1, 2, 3, 4, 5]

Final result: [1, 2, 3, 4, 5]
"""
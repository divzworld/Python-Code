# # Que. 19 Sort a list of tuples by the sum of all elements in the tuple.
# data = [(1, 2), (3, 1, 5), (2, 2)]
# # Expected → [(1, 2), (2, 2), (3, 1, 5)]

data = [(1, 2), (3, 1, 5), (2, 2)]

sorted_list = sorted(data, key = lambda x : sum(x))
print(sorted_list)

"""
🧠 INTERVIEW TAKEAWAY

This shows you understand:

Using lambda to compute a custom key

Using sum() to aggregate tuple values

Sorting based on computed values (not just the raw tuple)

If asked:

"Could you sort descending?"
You just add reverse=True.
"""
# Que.07 7. Given a list of words, sort them by length using lambda.

"""
🧠 TEACHER HINT TO FIX

Think about what key= expects: a function that takes ONE element and returns a value used for sorting.

Your element here is x (a string).

What do we want? Its length.

So your lambda should simply return len(x).

🧠 INTERVIEW-LEVEL EXPLANATION

"We use len(x) because len() is a built-in function that takes an object and returns its length. Passing x gives the length of each string, which becomes the sorting key."
"""

data = ["Divya" , "Rudra" , "Chitralekha" , "Sukruti" , "Nikie" , "Rajveer"]
result = sorted(data, key = lambda x : len(x))

print(result)
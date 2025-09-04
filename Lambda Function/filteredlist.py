# Que.10  From a list of names, filter those with length > 5 characters.

names = ["Divya" , "Rudra" , "Shree" , "Devika" , "Gayatri", "Smera" , "Asavari"]

result = list(filter(lambda x : len(x)>5 , names)) #"Using filter() is more Pythonic and concise. It directly expresses that we are selecting elements based on a condition, rather than manually building a new list."
print(result) 
# Que.22  Given a sentence, return words sorted by their frequency.
"""
-- Meaning of question

Step-by-step:

You are given a string like:
"apple banana apple orange banana apple"

Count how many times each word appears:

apple → 3

banana → 2

orange → 1

Then sort the words by how many times they appeared (highest first):

['apple', 'banana', 'orange']
Because apple appeared the most, then banana, then orange.
"""

data = ["Pineapple","Kiwi","Watermelon","Dragonfruit","Pineapple","Pineapple","Pineapple","Watermelon","Watermelon","Kiwi"]

result = sorted(set(data), key = lambda x : data.count(x),reverse = True)

print(result)
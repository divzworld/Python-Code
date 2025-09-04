# Que.23 Filter words with vowels > 2 using lambda.
"""
🧠 What the Question is Asking
"Filter words with vowels > 2 using lambda."
Step-by-step meaning:

You have a list of words, e.g.
["apple", "sky", "education", "python"]
For each word, count how many vowels (a, e, i, o, u) it has:
apple → a,e → 2 vowels
sky → y (not counted normally) → 0 vowels
education → e,u,a,i,o → 5 vowels
python → o → 1 vowel
Keep only those words where vowel count > 2
Output should be: ["education"] (because only that has > 2 vowels)
"""
data = ["banana","airoplane","suitcase","fly","cry","cart"]
result = list(filter(lambda x : (sum(1 for char in x if char in "aeiou") )> 2 , data ))

print(result)
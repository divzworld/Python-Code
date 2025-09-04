# Que.09 Create a lambda that returns True if a string starts with 'A', else False

str = input(" Enter string : ").capitalize()

result = lambda x : x.startswith("A") 

print(result(str))
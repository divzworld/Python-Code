# Que.20 Filter palindromes using lambda.
# words = ["madam", "hello", "racecar"]
# Output → ['madam', 'racecar']

words = ["madam", "hello", "racecar"]
result = list(filter(lambda x : x ==  x[::-1] , words))

print(result)
# Que.25 Build a single-line lambda that returns True if a number is:
# ○ divisible by 3
# ○ OR greater than 50
# ○ AND not equal to 99

num = int(input(" What's num ? "))
result = lambda x : True if (x % 3 == 0 or x > 50) and x != 99 else False

print(result(num))


"""
🧠 INTERVIEW TAKEAWAY

If asked:

"Why did you use parentheses?"

Say:

"Because and has higher precedence than or, 
so without parentheses the logic would be evaluated wrong. Grouping makes it explicit and avoids subtle bugs."

"""
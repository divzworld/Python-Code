# Que.13 Using map(), return a list of pass/fail strings based on marks.
# Output: ['Fail', 'Pass', 'Pass']

marks = [32,80,75]
result = list(map(lambda x : "Pass" if x > 35 else "Fail", marks))
print(result)

"""
🧠 TEACHER'S INTERVIEW NOTE

This is interview-ready code — clean, no extra loops, no if-statements outside lambda.
If they ask "Why not use filter?" you can say:

"Filter() would remove the failing students entirely, but here I need both pass and fail as output, so map() is the right choice."
"""
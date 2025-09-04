# Que. Write a lambda that returns True if the string starts with any vowel (A, E, I, O, U), otherwise False.

"""
🧠 INTERVIEW-LEVEL EXPLANATION

If asked in an interview:
“Why use a tuple with startswith()?”

Answer like a pro:

"startswith() accepts a tuple, so it checks each option inside that tuple until it finds a match. 
It’s cleaner and faster than chaining multiple or conditions manually."
"""

str = input(" Enter a string : ").lower()

result = lambda x : x.startswith(("a","e","i","o","u"))  #startswith() can check for multiple options at once if you pass it a tuple.
print(result(str))
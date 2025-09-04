# Que.05  Combine map + filter: double the numbers that are odd from [1,2,3,4,5,6]
"""
---- I done this mistakes before this correct program
doublelist = map(lambda x : x * 2 , oddlist)
print(list(doublelist))  # ❌ gives [] because oddlist is now empty

🧠 WHY THIS HAPPENS (The Big Lesson)

-filter() and map() return iterators — they are like one-time-use generators.

-Once you loop through them (like converting to list), they are done, you can't reuse them.

-If you need to use them multiple times, store the result in a list first.
"""
number = [1,2,3,4,5,6]


oddlist = list(filter(lambda x : x%2 != 0 , number))
print(oddlist)


doublelist = list(map( lambda x : x * 2 , oddlist))
print(doublelist)
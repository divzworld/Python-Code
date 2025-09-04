# Que.14 Given prices in dollars [10, 20, 30], convert to rupees (x 83.2)

dollars = [10, 20, 30]
rupees = list(map(lambda x : x * 83.2 , dollars))

print(rupees)
# Que.16  Sort a list of dictionaries by a key inside dictionary.
# products = [{"name": "A", "price": 300}, {"name": "B", "price": 100}]
# Sort by price → [{'name': 'B', 'price': 100}, {'name': 'A', 'price': 300}]


products = [{"name": "A", "price": 300}, {"name": "B", "price": 100}]

sorted_dict = sorted(products, key = lambda x : x["price"] )
print(sorted_dict)
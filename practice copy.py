from collections import Counter

items = [1, 2, 2, 3, 4, 4, 4, 5, 1]
counter = Counter(items)
print(counter)
first_unique = next(iter({key: value for key, value in counter.items() if value == 1}))
print(first_unique)
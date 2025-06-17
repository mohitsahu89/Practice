from collections import Counter

items = [1, 2, 2, 3, 4, 4, 4, 5, 1]
counter = Counter(items)
first_unique = next(iter({key: value for key, value in counter.items() if value == 1}))
print(first_unique)


longest_string = "Neighbourhood"
read = ""
for i in longest_string:
    if i not in read:
        read += i  
    else:
        break
print(read)
a_list = [3, 1, 2, 3, 4, 7, 4, 6, 8, 4, 1, 9]

map = list(map(lambda x: x*2, a_list))
print(map)

filter = list(filter(lambda x: x > 5, a_list))

print(filter)

first_val = next(iter(sorted(a_list)))

print(first_val)
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

# Reverse String
string = "Hello World!"

print(string[::-1])


# Palindrome String Check
palin_str = "Malayalam"

print(palin_str.lower() == ((palin_str[::-1]).lower()))

# Fibonacci Series

fibo = []
num = 3

if num <= 2:
    for _ in range(num):
        fibo.append(_)
elif num > 2:
    x, y, z = 0, 1, None

    fibo.append(x)
    fibo.append(y)
    for _ in range(1, num - 1):
        z = x + y
        fibo.append(z)
        x, y = y, z

print(fibo)

max_list = [14, 35, 42 , 78, 92, 79, 18]
print(min(max_list))
print(max(max_list))

max_list.sort(reverse=True)
print(max_list[0])

max = 0
for _ in max_list:
    if not max > _:
        max = _

print(max)

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for c in vowels:
    if c in longest_string:
        count += 1
print(count)

print(sum(1 for c in str(set(longest_string.lower())) if c in 'aeiou'))
print(str(sorted(set(longest_string.lower()))))
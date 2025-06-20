# def two_sum(num_list: list, target):
#     return [num_list.index(value) for value in num_list if (target - value) in set(num_list)]


# print(two_sum([7, 3, 5, 15], 12))

# from collections import defaultdict


# anagram_list = ["bat", "tab", "eat", "tea", "tan", "ate", "nat"]
# final = defaultdict(list)

# for index, word in enumerate(anagram_list):
#     key = ''.join(sorted(word))
#     final[key].append(word)

# print(final.values())

from collections import Counter

longest_string = "Neighbourhood"
values = next(iter([{key: value} for key, value in Counter(longest_string).items() if value == 1]))
print(values)

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # for row in matrix:
    #     row.reverse()
    return matrix

# Example
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(rotate(matrix))

my_list = []
n = len(matrix)
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[(n-1) - j][i])
    my_list.append(row)

print(my_list)
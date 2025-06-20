

# input = 4

X000X
0X0X0
00X00
0X0X0
X000X



# for outer in range(input):
#     inner_list = []
#     for inner in range(input):
#         if inner % 2 == 0:
#             inner_list.append('X')
#         else:
#             inner_list.append('0')
#     print(inner_list)






# Problem Description
# You have given a string A having Uppercase English letters.
# You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.


# Problem Constraints
# 1 <= length(A) <= 105


# Input Format
# First and only argument is a string A.


# Output Format
# Return an long integer denoting the answer.


# Example Input
# Input 1:



A = "ABCGAGABCG"
# Input 2:
# A = "GAB"
cnt = 0
for i in range(len(A)):
    if A[i] == 'A':
        new_str = A[i:]
        for j in range(len(new_str)): # BCGAG
            if new_str[j] == 'G':
                cnt += 1

print(cnt)

A = "ABCGAG"
cnt = 0
g_count = 0

for ch in reversed(A):
    print(ch)
    if ch == 'G':
        g_count += 1
    elif ch == 'A':
        cnt += g_count

print(cnt)
        





# Example Output
# Output 1:



# 3
# Output 2:
# 0



# Example Explanation
# Explanation 1:


# Subsequence "AG" is 3 times in given string, the pairs are (0, 3), (0, 5) and (4, 5).
# Explanation 2:
# There is no subsequence "AG" in the given string


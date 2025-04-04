# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

# Input:
# [100, 200, 1, 3, 2, 4]
# Output:
# 4
# Explanation:
# The longest consecutive subsequence is 1, 2, 3, and 4.

# Input:
# [3, 8, 5, 7, 6]
# Output:
# 4
# Explanation:
# The longest consecutive subsequence is 5, 6, 7, and 8.
arr = [3, 8, 5, 7, 6]
arr.sort()
# 3 5 6 7 8

def longest_Consecutive(arr):
    num_set = set(arr)
    max_len = 0
    for num in arr:
        if num-1 not in num_set:
            current_num = num
            current_len = 1
            while current_num+1 in num_set:
                current_num+=1
                current_len+=1
            max_len = max(max_len,current_len)
    return max_len

print(longest_Consecutive(arr))
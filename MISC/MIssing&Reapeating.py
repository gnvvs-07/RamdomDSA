# https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

# Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

# Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].

# Examples:

# Input: arr[] = [2, 2]
# Output: [2, 1]
# Explanation: Repeating number is 2 and smallest positive missing number is 1.
# Input: arr[] = [1, 3, 3] 
# Output: [3, 2]
# Explanation: Repeating number is 3 and smallest positive missing number is 2.

arr = [1, 3, 3]
n = len(arr)

freq,repeating,nthSum,current_sum = {},None,n*(n+1)//2,0

for num in arr:
    freq[num] = freq.get(num,0)+1
    current_sum+=num
    if freq[num] == 2:
        repeating = num

missing = nthSum-(current_sum-repeating)

print([repeating, missing])
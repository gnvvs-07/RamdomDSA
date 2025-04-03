# LeetCode 560 : https://leetcode.com/problems/subarray-sum-equals-k/description/

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
 
# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

arr = list(map(int,input().split()))
target = int(input())
# brute force

count = 0
output = []
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if sum(arr[i:j+1]) == target:
            output.append(arr[i:j+1])

print(len(output))

# optimal approach - prefix sum



# 👇code not working
# def generator(arr, target, index=0, ds=None, ans=None):
#     if ds is None:
#         ds = []
#     if ans is None:
#         ans = []
#     if index >= len(arr):
#         if sum(ds) == target: 
#             ans.append(ds[:])
#         return
#     ds.append(arr[index])
#     generator(arr, target-arr[index], index + 1, ds, ans)
#     ds.pop()
#     generator(arr, target, index + 1, ds, ans)
#     return ans

# print(len(generator(arr,target)))




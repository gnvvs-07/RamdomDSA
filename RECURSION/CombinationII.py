# leetcode 40 : https://leetcode.com/problems/combination-sum-ii/description/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
_input = list(map(int,input().split()))
l = len(_input)
candidates = _input[:l-1]
target = _input[l-1]

def combinations1(index,target,candidates,ds=None,ans=None):
    if ds is None:
        ds = []
    if ans is None:
        ans = []
    if target == 0:
        ans.append(ds[:])
        return ans
    for i in range(index,len(candidates)):
        if i>index and candidates[i] == candidates[i-1]:
            continue
        if candidates[i]>target:
            break
        ds.append(candidates[i])
        combinations1(i+1,target-candidates[i],candidates,ds,ans)
        ds.pop()
    return ans

ans = combinations1(0,target,sorted(candidates))
for combination in ans:
    print(combination)
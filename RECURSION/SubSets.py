# Leet code 78 : https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

arr = list(map(int,input().split()))

def generator(arr,ans=None,index=0,ds=None):
    if ans == None:
        ans = []
    if ds == None:
        ds = []
    if index>=len(arr):
        ans.append(ds[:])
        return ans
    ds.append(arr[index])
    generator(arr,ans,index+1,ds) 
    ds.pop()
    generator(arr,ans,index+1,ds)
    return ans

for array in reversed(generator(arr)):
    print(array)
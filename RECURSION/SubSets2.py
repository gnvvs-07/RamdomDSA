# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# IMPORTANT : the subsets can start from any value in the array 
arr = list(map(int,input().split()))

def generator(arr,index=0,ds=None,ans=None):
    if ds is None:
        ds = []
    if ans is None:
        ans=[]
    # soting at the begining 
    if index==0:
        arr.sort()
    ans.append(ds[:])
    for i in range(index,len(arr)):
        if i!=index and arr[i] == arr[i-1]:
            continue
        ds.append(arr[i])
        generator(arr,i+1,ds,ans)
        ds.pop()
    return ans

for array in generator(arr):
    print(array)
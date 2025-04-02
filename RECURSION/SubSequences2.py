# Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

# Examples:

# Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
# Output: 3
# Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.

arr = list(map(int,input().split()))
target = int(input())
def subsets(arr,index=0,ds=None,ans=None):
    if ds is None:
        ds=[]
    if ans is None:
        ans=[]
    if sum(ds)==target:
        ans.append(ds[:])
        return ans
    for i in range(index,len(arr)):
        ds.append(arr[i])
        subsets(arr,i+1,ds,ans)
        ds.pop()
    return ans

for arrays in (subsets(arr)):
    print(arrays)
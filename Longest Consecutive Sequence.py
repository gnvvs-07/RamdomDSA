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

def generator(arr,ds=None,ans=None,index=0):
    arr.sort()
    if ds==None:
        ds=[]
    if ans == None:
        ans = []
    # base condition
    if index == len(arr):  # base case
        if ds:
            ans.append(ds[:])
        return ans 
    if not ds or arr[index] == ds[-1]+1:
        ds.append(arr[index])
        generator(arr,ds,ans,index+1)
        ds.pop()
    generator(arr,[],ans,index+1)
    return ans

def max_lengths(arr):
    count = 0
    for row in arr:
        count = max(count,len(row))
    return count

print(max_lengths(generator(arr)))



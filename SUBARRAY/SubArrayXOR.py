# Subarray with given XOR

# Given an array of integers A and an integer B.

# Find the total number of subarrays having bitwise XOR of all elements equals to B.

# Problem Constraints
# 1 <= length of the array <= 105
# 1 <= A[i], B <= 109

# Input Format
# The first argument given is the integer array A.
# The second argument given is integer B.

# Output Format
# Return the total number of subarrays having bitwise XOR equals to B.

# Example

# Input 1:
#  A = [4, 2, 2, 6, 4]
#  B = 6
# Output 1:
#  4
# Explanation 1:
#  The subarrays having XOR of their elements as 6 are:
#  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

# Input 2:
#  A = [5, 6, 7, 8, 9]
#  B = 5
# Output 2:
#  2
# Explanation 2:
#  The subarrays having XOR of their elements as 5 are :
# [5] and [5, 6, 7, 8, 9]


def XOR_array(arr):
    result = 0
    result ^= (num for num in arr)
    return result

def generator(arr,target,index = 0,ds = None,ans=None):
    if ds is None:
        ds= []
    if ans is None:
        ans = []
    if XOR_array(ds) == target:
        ans.append(ds[:])
        return 
    if index<len(arr):
        ds.append(arr[index])
        generator(arr,target,index+1,ds,ans)
        ds.pop()
    generator(arr,target,index+1,ds,ans)
    return ans

A = [5, 6, 7, 8, 9]
B = 5

for row in generator(A,B):
    print(*row)

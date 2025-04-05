# Leet Code 493 Reverse Pairs : https://leetcode.com/problems/reverse-pairs/description/

# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -231 <= nums[i] <= 231 - 1

# arr = [2,4,3,5,1]
arr = [1,3,2,3,1]
def MergeSort(arr,low,high):
    cnt = 0
    if low>=high:
        return 0
    mid = (low+high)//2
    # return MergeSort(arr,left,mid)+MergeSort(arr,mid+1,right)+countPairs(arr,left,mid,right)
    mid = (low + high) // 2
    cnt += MergeSort(arr, low, mid)  # left half
    cnt += MergeSort(arr, mid + 1, high)  # right half
    cnt += countPairs(arr, low, mid, high)  # Modification
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def countPairs(arr,low,mid,high):
    right=mid+1
    count = 0
    for i in range(low,mid+1):
        while right<=high and arr[i]>2*arr[right]:
            right+=1
        count+=right-(mid+1)
    return count

def merge(arr,left,mid,right):
    count = 0
    output = []
    i = left
    j = mid + 1
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            output.append(arr[i])
            i+=1
        else:
            output.append(arr[j])
            j+=1
    
    while i<=mid:
        output.append(arr[i])
        i+=1
    while j<=right:
        output.append(arr[j])
        j+=1
    for k in range(len(output)):
        arr[left + k] = output[k]

print(MergeSort(arr,0,len(arr)-1))
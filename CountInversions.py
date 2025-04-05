# https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

# Given an array of integers arr[]. Find the Inversion Count in the array.
# Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
# If an array is sorted in the reverse order then the inversion count is the maximum. 

# Examples:

# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
# Input: arr[] = [2, 3, 4, 5, 6]
# Output: 0
# Explanation: As the sequence is already sorted so there is no inversion count.

arr = [2,4,1,3,5]
def MergeSort(arr,left,right):
    if left>=right:
        return 0
    mid = (left+right)//2
    return MergeSort(arr,left,mid)+MergeSort(arr,mid+1,right)+merge(arr,left,mid,right)
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
            count+=(mid-i+1)
            j+=1
    
    while i<=mid:
        output.append(arr[i])
        i+=1
    while j<=right:
        output.append(arr[j])
        j+=1
    for k in range(len(output)):
        arr[left + k] = output[k]
    return count

print(MergeSort(arr,0,len(arr)-1))
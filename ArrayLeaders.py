# You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

# Examples:

# Input: arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
# Input: arr = [10, 4, 2, 4, 1]
# Output: [10, 4, 4, 1]
# Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
import time as t
arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
start = t.time()
output = []
for i in range(n):
    suffix = arr[i+1:]
    if arr[i]>max(suffix,default=float('-inf')):
        output.append(arr[i]) 


print(output)
end = t.time()
print(f"Time taken: {end - start:.6f} seconds")
# optimized 
def leaders(arr):
        # code here
        start = t.time()
        n = len(arr)
        output = []
        max_so_far = float('-inf')

        for i in range(n - 1, -1, -1):  # Traverse from right to left
            if arr[i] >= max_so_far:
                output.append(arr[i])
                max_so_far = arr[i]  # Update max_so_far

        print(output[::-1])
        end = t.time()
        print(f"Time taken: {end - start:.6f} seconds")
leaders(arr)
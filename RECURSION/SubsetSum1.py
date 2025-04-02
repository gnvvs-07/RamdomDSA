# Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.

# Examples:

# Input: arr[] = [2, 3]
# Output: [0, 2, 3, 5]
# Explanation: When no elements are taken then Sum = 0. When only 2 is taken then Sum = 2. When only 3 is taken then Sum = 3. When elements 2 and 3 are taken then Sum = 2+3 = 5.

arr = list(map(int,input().split()))
def generator(arr,ans = None,index=0,sum=0):
    if ans is None:
        ans = []
    if index>=len(arr):
        ans.append(sum)
        return ans
    generator(arr,ans,index+1,sum+arr[index])
    generator(arr,ans,index+1,sum)
    if index ==0:
        return sorted(ans)
    return ans 

for _sum in generator(arr):
    print(_sum)


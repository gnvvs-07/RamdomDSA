arr = list(map(int,input().split()))
n = len(arr)

# 2 pointer approach
def reverse_2p(arr,l,r):
    if (l>=r):
        return 
    arr[l],arr[r] = arr[r],arr[l]
    reverse_2p(arr,l+1,r-1)
# reverse_2p(arr,0,n-1)
# print(arr)

# using single pointer
def reverse_1p(arr,i):
    n = len(arr)
    if (i>=n//2):
        return 
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    reverse_1p(arr,i+1)
reverse_1p(arr,i=0)
print(arr)
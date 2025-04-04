# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# [
    # [1]           max_cols=1,row=1
    # [1,1]         max_cols=2,row=2
    # [1,2,1]       max_cols=3,row=3
    # [1,3,3,1]     max_cols=4,row=4
    # [1,4,6,4,1]   max_cols=5,row=5

# ]       

# [i][j] = rCc

def nCr(n,r):
    r = min(r,n-r)
    if r>n:
        return 0
    if r==0 or r==n:
        return 1
    if r==1:
        return n
    return (n*nCr(n-1,r-1))//r
def pascal(n):
    output = []
    for i in range(n):
        row = []
        for j in range(i+1):
            row.append(nCr(i,j))
        output.append(row)
    return output

# Example 2:
# Input: numRows = 1
# Output: [[1]]

n = int(input())

for row in pascal(n):
    print(*row)


# GRID UNIQUE PATHS - COUNT paths in matrix
def numberOfPaths(m,n):
    if m == 1 or n ==1:
        return 1
    return numberOfPaths(m-1,n)+numberOfPaths(m,n-1)

print(numberOfPaths(5,3))   #5×3
print(numberOfPaths(3,3))   #3×3
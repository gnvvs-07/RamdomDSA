# Generate all binary strings without consecutive 1’s

# Given an integer, K. Generate all binary strings of size k without consecutive 1’s.

# Examples: 

# Input : K = 3  
# Output : 000 , 001 , 010 , 100 , 101 
# Input : K  = 4 
# Output :0000 0001 0010 0100 0101 1000 1001 1010
n = int(input())
def generate_binary(n):
    if n==0:
        return [""]
    if n==1:
        return ["0","1"]
    res = []
    for s in generate_binary(n-1):
        res.append(s+"0")
        if s[-1]!="1":
            res.append(s+"1")
    return res

for binaryStrings in generate_binary(n):
    print(binaryStrings)
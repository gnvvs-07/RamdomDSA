# contiguous as well as non contiguous(follows the order) => subsequence
# only contigous(follows the order) =>sub array

# [3,1,2]
arr = list(map(int,input().split()))
n = len(arr)
def generator(index=0,output=None):
    if output == None:
        output = []
    if index>=n:
        print(output)
        return 
    else:
        output.append(arr[index])
        generator(index+1,output)
        output.pop()
        generator(index+1,output)

generator()
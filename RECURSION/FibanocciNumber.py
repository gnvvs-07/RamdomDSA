# Example for multiple recursion calls
# 0,1,1,2,3,5,8,.................
# f(n) = f(n-1)+f(n-2)
import sys

n = int(input())

if n>sys.maxsize:
    raise ValueError("Error integer limit exceeded")

def nthFibanocci(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return nthFibanocci(n-1)+nthFibanocci(n-2)
    # first nthFibanocci(n-1)[and its successors i.e nthFibanocci(n-1-1){repeat again it will be completed first and then goes to nthFibanocci(n-1-2)} and nthFibanocci(n-1-2)] will be completed and then nthFibanocci(n-2)
print(nthFibanocci(n))
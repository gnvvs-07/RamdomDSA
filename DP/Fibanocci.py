n = int(input("Enter input: "))

# using recursion
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)
    
result_recursion = fib(n)

print(result_recursion)

# problem is overlapping sub problems
# fib(n-2) is calcuated before fib(n-1) but it recomputes for the second recurion fib(n-1)
# solution is memorization store the values of problems in some map/table(1D or 2D arrays)

# using Dynamic Programming(Memorization)

def dp_memo(n, memory={}):
    if n in memory:
        return memory[n]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        res = dp_memo(n-2, memory) + dp_memo(n-1, memory)
        memory[n] = res
        return res

result_dp = dp_memo(n)

print(result_dp)

# This takes n steps but for very larger inputs it fails
# T(n) = O(n)
# S(n) = O(n)[recursion stack space]+O(n)[dp array]
# solution : Tabulation (bottom-up) 

# memorization or recursion =>solution->Null(base case)
# bottom up => base case to required case(Null->solution)

# Tabulation(bottom-up) approach

def dp_table(n, dp=None):
    if dp is None:
        dp = [0] * (n + 1)  # Initialize dp list with size n+1
    # base cases
    if n >= 1:
        dp[0] = 0   # n=1 should correspond to index 0 for conventional Fibonacci
    if n >= 2:
        dp[1] = 1   # n=2 should correspond to index 1
    # table construction from base cases
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n-1]

result_dp_table = dp_table(n)

print(dp_table(n))
# T(n) = O(n)
# S(n) = O(n)[no stack space is required]

# Now how to remove the O(n) space complexity from the tabular approach

def dp_table_optimized(n):
    prev2 = 0
    prev = 1
    if n == 1:
        return 0   
    if n == 2:
        return 1   
    for i in range(2, n):
        current = prev+prev2
        prev2 = prev
        prev = current
    return prev

# T(n) = O(n-2)
# S(n) = k

print(dp_table_optimized(n))
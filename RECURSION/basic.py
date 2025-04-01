def recursive_fun(n=1):
    if n == 3:
        return n
    return n*recursive_fun(n+1)

print(recursive_fun())
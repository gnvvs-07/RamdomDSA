# Leet code 22 : https://leetcode.com/problems/generate-parentheses/description/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

n = int(input)
def valid(parenthesis):
    stack = []
    for ch in parenthesis:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# print(valid("()(())"))

def generate(x,index=0,ds=None,ans=None,available=None):
    if ds is None:
        ds = []
    if ans is None:
        ans = []
    if available is None:
        available = ["(",")"]
    n = 2*x
    if valid(ds[:]):
        ans.append(ds[:])
        return ans
    if len(ds)<n:
        ds.append("(")

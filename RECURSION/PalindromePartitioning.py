# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def generate_palindromes(s: str, index=0, ds=None, ans=None):
    if ds is None:
        ds = []
    if ans is None:
        ans = []
    
    if index == len(s):  
        ans.append(ds[:])
        return
    
    for i in range(index, len(s)):
        substring = s[index:i+1]
        if is_palindrome(substring):  
            ds.append(substring)
            generate_palindromes(s, i+1, ds, ans)  
            ds.pop() 
    
    return ans

s = input("Enter a string: ")
result = generate_palindromes(s)
print(result)

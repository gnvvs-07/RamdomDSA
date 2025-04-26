# Leet code : 139 :https://leetcode.com/problems/word-break/description/

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

def generator(s,wordDict,index=0):
    if index == len(s):
        return "true"
    i = 0
    while i<max(list(len(num)for num in wordDict)) and (index+i)<len(s):
        if s[index:index+1] not in set(wordDict):
            i+=1
        generator(s,wordDict,index+i+1)
        i=0
    return "false"

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(generator(s,wordDict))

s1 = "applepenapple"
wordDict1 = ["apple","pen"]
print(generator(s1,wordDict1))
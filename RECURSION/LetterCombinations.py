# LeetCode 17 : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 
# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from itertools import product

n = int(input())
mapper = [
    "",                 # 0
    "",                 #1
    "abc",              #2
    "def",              #3
    "ghi",              #4
    "jkl",              #5
    "mno",              #6
    "pqrs",             #7
    "tuv",              #8
    "wxyz"              #9
]

def letters_available(n):
    return list(str(n))

digits = letters_available(n)

def cross_product(*s):
    return [''.join(pair) for pair in product(*s)]

required_strings = []

for digit in digits:
    index = int(digit)
    required_strings.append(mapper[index])

if required_strings:
    print(cross_product(*required_strings))
else:
    print([])
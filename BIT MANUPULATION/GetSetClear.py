# Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 

# 1. Get ith bit

# 2. Set ith bit

# 3. Clear ith bit

# Note : For better understanding, we are starting bits from 1 instead 0. (1-based). You have to print space three space separated values ( as shown in output without a line break) and do not have to return anything.

# Examples :

# Input: 70 3
# Output: 1 70 66
# Explanation: Bit at the 3rd position from LSB is 1. (1 0 0 0 1 1 0) .The value of the given number after setting the 3rd bit is 70. The value of the given number after clearing 3rd bit is 66. (1 0 0 0 0 1 0)
# Input: 8 1
# Output: 0 9 8
# Explanation: Bit at the first position from LSB is 0. (1 0 0 0)  .The value of the given number after setting the 1st bit is 9. (1 0 0 1).  The value of the given number after clearing 1st bit is 8. (1 0 0 0)

num, position = map(int, input().split())

def get(num, pos):
    value = 1 << (pos - 1)  # Shift 1 to the left (pos-1) times
    print((num & value) >> (pos - 1))  # Extract the bit value

get(num, position)

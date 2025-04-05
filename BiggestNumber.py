# Arrange given numbers to form the biggest number

import math

arr = [54, 546, 548, 60]

def max_number_digits(arr):
    max_value = max(arr)
    if max_value == 0:
        return 1
    return math.floor(math.log10(abs(max_value))) + 1

def make_same(arr):
    digits = max_number_digits(arr)
    result = []
    for num in arr:
        num_digits = math.floor(math.log10(abs(num))) + 1
        multiplier = 10 ** (digits - num_digits)
        result.append(num * multiplier)
    return result

print(make_same(arr))  # Output: [540, 546, 548, 600]

make_same_arr = make_same(arr)

freq = {}
n = len(arr)
for i in range(n):
    freq[i] = make_same_arr[i]
    
sorted_dict = dict(sorted(freq.items(),key=lambda item:item[1]))

output = []
for i in sorted_dict:
    output.append(arr[i])

print(output)       #[54, 546, 548, 60]
s = ""
for num in reversed(output):
    s+=str(num)
    
print(int(s))

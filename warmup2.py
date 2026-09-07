def string_times(str, n):
    larger_str = str * n
    return larger_str

def front_times(str, n):
    if len(str) == 1 or len(str) == 2:
        return str * n
    else:
        front = str[0:3]
        return front * n

def string_bits(str):
    return_str = ""
    for i in range(0, len(str), 2):
        return_str += str[i]
    return return_str

def string_splosion(str):
    a = len(str)
    return_str = ""
    for i in range(0, a):
        substr = str[0:i]
        return_str += substr
    return return_str + str

def last2(str):
    max = 0
    last2 = str[len(str)-2:]
    for i in range(0, len(str)-2):
        substr = str[i:i+2]
        if substr == last2:
            max += 1
        
    return max

def array_count9(nums):
    return nums.count(9)

def array_front9(nums):
    if len(nums) < 4:
        return nums.count(9) >= 1
    else:
        return nums[0:4].count(9) >= 1
        

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

def array123(nums):
    for i in range(0, len(nums)-2):
        if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
            return True
    return False

def string_match(a, b):
    count = 0
    str = ""
    if len(a) <= len(b):
        str = a
    else:
        str = b
    for i in range(0, len(str)-1):
        if(a[i:i+2] == b[i:i+2]):
            count += 1
    return count
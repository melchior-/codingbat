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

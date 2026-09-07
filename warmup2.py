def string_times(str, n):
    larger_str = str * n
    return larger_str

def front_times(str, n):
    if len(str) == 1 or len(str) == 2:
        return str * n
    else:
        front = str[0:3]
        return front * n
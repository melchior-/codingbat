def make_bricks2(small, big, goal):
    sum = 0
    for i in range(small):
        sum += 1
        if sum == goal:
            return True
    for i in range(big):
        sum += 5
        if sum == goal:
            return True
    return False

def make_bricks(small, big, goal):
    if goal > big * 5 + small:
        return False
    reminder = goal % 5
    if small - reminder < 0:
        return False
    return True

def lone_sum(a, b, c):
    sum = a + b + c
    if (a == b or a == c):
        sum -= a
    if (b == a or b == c):
        sum -= b
    if (c == a or c == b):
        sum -= c
    return sum

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n == 15:
        return 15
    if n == 16:
        return 16
    if n >= 13 and n <= 19:
        return 0
    return n

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    mod = num % 10
    if mod >= 5:
        return (10 - mod) + num
    else:
        return num - mod

def close_far(a, b, c):
    close_b = abs(a-b)
    close_c = abs(a-c)
    if close_b <= 1 and close_c >= 2:
        if(abs(c-b) >= 2):
            return True
    elif close_b >= 2 and close_c <= 1:
        if(abs(b-c) >= 2):
            return True
    return False

def make_chocolate(small, big, goal):
    if goal > big * 5 + small or goal % 5 > small:
        return -1
    reminder = goal % 5
    if (big * 5 < goal):
        return (goal - (big*5))
    return reminder
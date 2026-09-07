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
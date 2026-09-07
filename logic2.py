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


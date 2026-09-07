def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

def big_diff(nums):
    lol1 = max(nums)
    lol2 = min(nums)
    return lol1-lol2

def centered_average(nums):
    m = max(nums)
    s = min(nums)
    sum = 0
    for num in nums:
        sum += num
    sum -= m
    sum -= s
    return int(sum/(len(nums)-2))

def sum13(nums):
    if len(nums) == 0:
        return 0
    sum = 0
    prev13 = False
    for num in nums:
        if prev13:
            prev13 = False
            continue
        if (num == 13):
            prev13 = True
            continue
        sum += num
    return sum

def sum67(nums):
    sum = 0
    prev6 = False
    for num in nums:
        if num == 6:
            prev6 = True
            continue
        if prev6:
            if num == 7:
                prev6 = False
            continue
        sum += num
    return sum

def has22(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False
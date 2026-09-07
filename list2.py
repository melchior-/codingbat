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

print(big_diff([10,3,5,6]))
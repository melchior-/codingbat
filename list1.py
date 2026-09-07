def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False

def make_pi():
    return [3,1,4]

def common_end(a,b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    return nums[0] + nums[1] + nums[2]
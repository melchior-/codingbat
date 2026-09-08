# Return the given string repeated n times.
def string_times(str, n):
    larger_str = str * n
    return larger_str


# Repeat the first three characters of the string n times.
# If the string has fewer than three characters, use the entire string.
def front_times(str, n):
    if len(str) == 1 or len(str) == 2:
        return str * n
    else:
        front = str[0:3]
        return front * n


# Return every other character, starting with the first character.
def string_bits(str):
    return_str = ""

    # Step through the string by twos to select characters at even indexes.
    for i in range(0, len(str), 2):
        return_str += str[i]

    return return_str


# Build a string from progressively longer prefixes.
# For example, "Code" becomes "CCoCodCode".
def string_splosion(str):
    a = len(str)
    return_str = ""

    # Add each prefix, starting with the first character.
    for i in range(0, a):
        substr = str[0:i]
        return_str += substr

    # Add the complete string at the end.
    return return_str + str


# Count how many times the final two-character substring appears earlier.
def last2(str):
    max = 0
    last2 = str[len(str)-2:]

    # Compare each two-character section with the final two characters.
    for i in range(0, len(str)-2):
        substr = str[i:i+2]
        if substr == last2:
            max += 1

    return max


# Count how many times the number 9 appears in the list.
def array_count9(nums):
    return nums.count(9)


# Check whether the first four elements contain a 9.
def array_front9(nums):
    if len(nums) < 4:
        return nums.count(9) >= 1
    else:
        return nums[0:4].count(9) >= 1


# Check whether the sequence 1, 2, 3 appears consecutively in the list.
def array123(nums):
    # Stop two positions before the end so a three-item sequence can fit.
    for i in range(0, len(nums)-2):
        if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
            return True

    return False


# Count matching two-character substrings at the same positions in both strings.
def string_match(a, b):
    count = 0
    str = ""

    # Use the shorter string to avoid checking beyond its length.
    if len(a) <= len(b):
        str = a
    else:
        str = b

    # Compare adjacent pairs at each possible starting position.
    for i in range(0, len(str)-1):
        if(a[i:i+2] == b[i:i+2]):
            count += 1

    return count
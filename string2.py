def double_char(str):
    return_str = ""
    for char in str:
        return_str += 2 * char
    return return_str

def count_hi(str):
    return str.count("hi")

def cat_dog(str):
    cats = str.count("cat")
    dogs = str.count("dog")
    if cats == dogs:
        return True
    else:
        return False

def count_code(str):
    count = 0
    for i in range(0, len(str)-3):
        if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
            count += 1
    return count


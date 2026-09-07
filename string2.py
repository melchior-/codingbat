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
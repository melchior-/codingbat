def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else:
        return False

def sum_double(a, b):
    sum = a + b
    if a == b:
        return 2*sum
    else:
        return sum

def diff21(n):
    diff = abs(n-21)

    if n > 21:
        return 2*diff
    else:
        return diff

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

def makes10(a, b):
    sum = a + b
    if a == 10 or b == 10 or sum == 10:
        return True
    else:
        return False

def near_hundred(n):
    diff = abs(n - 100)
    diff2 = abs(n - 200)
    if diff <= 10 or diff2 <= 10:
        return True
    else:
        return False

def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if a < 0 and b > 0:
            return True
        elif a > 0 and b < 0:
            return True
        else:
            return False

def not_string(str):
    prefix = str[:3]
    if prefix == "not":
        return str
    else:
        return "not " + str
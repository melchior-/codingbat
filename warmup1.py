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
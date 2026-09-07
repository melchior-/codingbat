def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    else:
        return cigars >= 40 and cigars <= 60

def date_fashion(you, date):
    if you >= 8 or date >= 8:
        if you <= 2 or date <= 2:
            return 0
        else:
            return 2
    elif you <= 2 or date <= 2:
        return 0
    else: return 1

def squirrel_play(temp, is_summer):
    if is_summer:
        return temp >= 60 and temp <= 100
    else:
        return temp >= 60 and temp <= 90

def caught_speeding(speed, is_birthday):
    increment = 0
    if is_birthday:
        increment = 5
    speed = speed - increment
    if speed <= 60:
        return 0
    elif speed >= 61 and speed <= 80:
        return 1
    else:
        return 2

def sorta_sum(a, b):
    sum = a+b
    if sum >= 10 and sum <= 19:
        sum = 20
    return sum

def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"
    else:
        if day == 0 or day == 6:
            return "10:00"
        else:
            return "7:00"

def love6(a, b):
    if a == 6 or b == 6 or a + b == 6 or abs(a-b) == 6:
        return True
    else:
        return False
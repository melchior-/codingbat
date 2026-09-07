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
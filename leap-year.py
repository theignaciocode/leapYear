def leapYear(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        else:
            return False
    else:
        return False


print(leapYear(2000))   # True
print(leapYear(2010))   # False
print(leapYear(2008))   # True
print(leapYear(1900))   # False
print(leapYear(1904))   # True

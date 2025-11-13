# Practices 91
def ordinalDate(day,month,year):
    days_before_mon = 0
    leap = bool((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))
    if month == 1:
        days_before_mon = 0
    elif month == 2:
        days_before_mon = 31
    elif month == 3:
        days_before_mon = 31 + (29 if leap else 28)
    elif month == 4:
        days_before_mon = 30 + (29 if leap else 28) + 31
    elif month == 5:
        days_before_mon = 30 + (29 if leap else 28) + 31 + 30
    elif month == 6:
        days_before_mon = 31 + (29 if leap else 28) + 31 + 30 + 31
    elif month == 7:
        days_before_mon = 31 + (29 if leap else 28) + 31 + 30 + 31 + 30
    elif month == 8:
        days_before_mon = 31 + (29 if leap else 28) + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        days_before_mon = 31 + (29 if leap else 28) + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        days_before_mon = 31 + (29 if leap else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        days_before_mon = 31 + (29 if leap else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        days_before_mon = 31 + (29 if leap else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30

    seqday = days_before_mon + day
    return seqday

def main():
    flag = True
    while flag :
        day = int(input("Enter a day: "))
        month = int(input("Enter a month: "))
        year = int(input("Enter a year: "))
        if day <=0 or day > 31:
            flag = False
        elif month < 1 or month > 12:
            flag = False
        elif year < 0:
            flag = False
        else:
            return ordinalDate(day,month,year)
    return "Invalid input!"

if __name__ == '__main__':
    print(main())














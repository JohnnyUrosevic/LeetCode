months_to_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

import datetime
def date_difference(a: datetime, b: datetime):
    year = b.year - a.year

    month = b.month - a.month
    month_diff = year * 12 + month

    day = b.day - a.day
    if day < 0:
        month_diff -= 1
        day = b.day + (months_to_days[a.month] - a.day) 

    return (month_diff, day)

if __name__ == "__main__":
    b = datetime.datetime(2019, 1, 1)
    a = datetime.datetime(2018, 12, 31)

    print(date_difference(a, b))
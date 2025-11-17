# Counting Sundays


#   - 1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

count = 0
day = 0
week_day = 0  # 0 monday - 6 Sunday
month = 0  # 0 Jan. - 11 Dec.
year = 1901
#
#  0 : Jan, 31 days
#  1:  Feb, 28 days
#  2:  Mar, 31 days
#  3:  Apr, 30 days
#  4:  May, 31 days
#  5:  Jun, 30 days
#  6:  Jul, 31 days
#  7:  Aug, 31 days
#  8:  Sep, 30 days
#  9:  Oct, 31 days
# 10:  Nov, 30 days
# 11:  Dec, 31 days
while year < 2001:
    day += 1
    week_day = (week_day + 1) % 7

    # Update Calendar
    if month in [3, 5, 8, 10] and day == 30:
        day = 0
        month = (month + 1) % 12
    if month in [0, 2, 4, 6, 7, 9, 11] and day == 31:
        day = 0
        if month == 11:
            year += 1
        month = (month + 1) % 12
    # February
    if month == 1:
        if year % 4 == 0 and day == 29:
            day = 0
            month = (month + 1) % 12
        elif year % 4 != 0 and day == 28:
            day = 0
            month = (month + 1) % 12

    print(
        f'{day+1:02}-{month+1:02}-{year} wd:{['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][week_day]}')

    # check for Monday at the first of the month
    if week_day == 6 and day == 1:
        count += 1

print(count)

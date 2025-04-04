import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    return isleap(year)

# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and not leap_year:
        return 28

# input user's name and age
name = input("input your name: ")
age = int(input("input your age: "))

# get the current local time
localtime = time.localtime(time.time())

# calculate the total number of years, months, and days
year = age
month = year * 12 + localtime.tm_mon
day = 0
begin_year = localtime.tm_year - year
end_year = begin_year + year

# calculate the total number of days in the years
for y in range(begin_year, end_year):
    if judge_leap_year(y):
        day += 366
    else:
        day += 365

# calculate the total number of days in the current year up to the current month
leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day += month_days(m, leap_year)

# add the current day of the month to the total number of days
day += localtime.tm_mday

# print the result
print(f"{name}'s age is {year} years or {month} months or {day} days")

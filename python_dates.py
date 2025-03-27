# python_dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

f_day = today.strftime("%d/%m/%Y")
print(f_day)

date_after_65_days = today + timedelta(days=65)
print(date_after_65_days)


# def days_between_dates(date1, date2):
#     date_format = "%Y-%m-%d"
#     d1 = datetime.strptime(date1, date_format)
#     d2 = datetime.strptime(date2, date_format)
#     return abs((d1 - d2).days)
#
# date1 = "2025-03-25"
# date2 = "2007-04-18"
#
# days_difference = days_between_dates(date1, date2)
# print(days_difference, 'days')

diff = date(2025, 3, 25)- date(2007, 4,18)
print(diff.days)
print(diff.days//7)


# def days_and_weeks_between_dates(date1, date2):
#     date_format = "%Y-%m-%d"
#     d1 = datetime.strptime(date1, date_format)
#     d2 = datetime.strptime(date2, date_format)
#     days = abs((d1 - d2).days)
#     weeks = days // 7
#     return days, weeks
#
# date1 = "2025-03-25"
# date2 = "2007-04-18"
#
# days, weeks = days_and_weeks_between_dates(date1, date2)
# print(f"Days: {days}, Weeks: {weeks}")
#

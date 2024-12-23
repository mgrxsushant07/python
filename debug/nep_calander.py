### Print Calendar of 2025
### Create Python Program That Convert Nepali Date To English and Vice Versa.
# pip install nepali-datetime
# import calendar
import nepali_datetime


# print(calendar.calendar(2024))
# print(calendar.calendar(2025))
# print(calendar.calendar(2026))

print(nepali_datetime.date.today())

nepali_datetime.date(2081, 9, 2).calendar()

for i in range(1,13):
    nepali_datetime.date(2081, i, 2).calendar()
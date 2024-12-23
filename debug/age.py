### Use current year to calculate his age.

import datetime as dt

age=int(input("Enter your age :"))
current_year=dt.datetime.now().year
year=current_year-age
print(f'Your age is {age} and your birth year is {year}')
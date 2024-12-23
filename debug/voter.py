
### Create A Program that check the person is voter or not using his birth year.

import datetime as dt

age=int(input("Enter your age :"))
current_year=dt.datetime.now().year
year=current_year-age

if age >=18:
    print(f'Your age is {age} and your birth year is {year}. You can vote. Thankyou...')
else:
    a=18-age
    print(f'Your age is less than 18. So,comeback after {a} years. Thankyou...')
    age=int(input('Enter your age :'))
    print('You can vote. Thankyou...')
    
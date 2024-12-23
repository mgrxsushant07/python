### If age >=18 then he is voter else not voter

import datetime as dt

age=int(input("Enter your age :"))
if age  < 18:
    a=18-age
    print(f'Your age is less than 18. So,comeback after {a} years. Thankyou...')
else:
    print('You can vote. Thankyou...')


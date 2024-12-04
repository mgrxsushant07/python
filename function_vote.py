#WAP to find out the person can vote or not.
#age over 18 can vote otherwise they can't vote.

age=int(input('Enter your age :'))
def vote(age):
    if age > 18:
        print(f'Your age is {age}. So, you can vote.')
    else :
        a=18-age
        print(f'Your age is {age}. SO, you cannot vote comeback after {a} years.')
vote(age)


              
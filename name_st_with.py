#continue
names=['Sushant','aryan','Saksham','Aayushs','Ankit','Nischal','Sailesh','Shudik','Rajan','Rajesh']
for i in names:
    if i.startswith('An'):
        continue 
    print(i) 

print()  ##this print is use for gap.

#break
fruits=['apple','banana','orange','mango','litichi','gravs']
for i in fruits:
    if i.startswith('o'):
        break
    print(i)

print() #for gap

#if any words are equal to 5 then it will automaticall skip it.
#for eg...
books=['Science','Nepali','Computer','Maths','English','Social','Economic','Accounting','Markiting']
for i in books:
    if len(i)==5:
        continue
    print(i)

print()#For gap purpose.....


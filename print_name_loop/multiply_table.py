#loop
#prg to make any nuber table.

number=int(input("Enter any muber :"))
for i in range(1,11):
    print(f"{number} * {i} = {i*number}")
     


#nested loop
for i in range(1,10):
    for j in range(1,11):
        print(f"{i} *{j} ={i*j}")
        print("/n")


#start and stop
star =2
end =5
for i in range(1,5):
    print(f"multiplication table of {i} is \n")
    for J in range(1,11):
        print(f"{i}*{J}={i*J}")
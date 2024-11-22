light=input("Enter traffic light. [Red,Yellow,Green]  ").lower

if light=="Red":
    print("Stop")
elif light=="Yellow":
    print("Ready to goo..")
elif light=="Green":
    print("Goo..")
else:
    print("Invalide light")
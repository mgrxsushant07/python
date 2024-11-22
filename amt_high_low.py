#WAP a prg if the amt is high or low than 500.

amt=int(input("Enter anmt :"))
if amt >=500:
    print("The Amount is high than 500.")
else:
    amt=500-amt
    print(f"The Amount is just {amt} lowest then 500.")
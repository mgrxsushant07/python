def voter():
    print("Welcome to the voter function.")
    age = int(input("Eter your age :"))
    if age >18:
        print(f"Your age is {age} So, You are eligible to vote.")

    else:
        a=18-age
        print(f"Your age is {age}. So, you are not eligible to vote. You can vote after {a} years.")

voter()
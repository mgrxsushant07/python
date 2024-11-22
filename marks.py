marks= int(input("Enter your score: "))
if marks >= 90:
    print("Congratulations you have got A+")
elif marks >= 80 and marks<=90 :
    print("Congratulations you have got A")
elif marks >= 70 and marks<=80:
    print("Congratulations you have got B+")
elif marks >= 60 and marks<=70:
    print("Congratulations you have got B")
elif marks >= 50 and marks<=60:
    print("Congratulations you have got C+")
elif marks >= 40 and marks<=50:
    print("Congratulations you have got C")
elif marks >= 35 and marks<=40:
    print("Congratulations you have got D+")
else:
    print("NonGraded(NG)")
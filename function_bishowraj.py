def result(mark):
    if mark >= 90 and mark <=100:
        return "A+"
    elif mark >=80 and mark <90:
        return "A"
    elif mark >=70 and mark <80:
        return "B+"
    elif mark >=60 and mark <70:
        return "B"
    elif mark >=50 and mark <60:
        return "C+"
    elif mark >=40 and mark <50:
        return "C" 
    elif mark >=30 and mark <40:
        return "D+"    
    elif mark >=20 and mark <30:
        return "D"
    elif mark >=0 and mark <20:
        return "E"
    else:
        return "Something went wrong"



students = {
    "ajaya": 80,
    "milan": 70,
    "suraj": 45,
    "achyut": 98
}

for name, mark in students.items():
    print(f"{name.capitalize()} mark is {mark} and grade is {result(mark)}")
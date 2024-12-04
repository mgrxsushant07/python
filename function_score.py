def calculate_grade(name,mark):
   if mark>=90 and mark>=100:
      print(f"{name} obtained A")
   elif mark>=80 and mark<90:
      print(f"{name} obtained B")
   elif mark>=70 and mark<80:
      print(F"{name} obtained C")
   elif mark>=60 and mark<70:
        print(F"{name} obtained D")
   else:
      print(f"{name} is failed ")
      
grades = {
   "John": 85,
   "Luna": 95,
   "sita": 75,
   "Gita": 30
}
for name, grade in grades.items():
   calculate_grade(name,grade)
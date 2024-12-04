score = {
    "suman": 90,
    "achyut": 95,
    "suraj": 80,
    "surya": 60
}
# A grade student is who took 90 or +

agrade = {name: mark for name, mark in score.items() if mark>=90}  
#{key_expression: value_expression for item in iterable if condition}#syntax use in agrade..
# key_expression = name(x)
#value_expression = mark(y)
#iterable = .items() (use have to give both name and mark)
#condition = mark>=90

print(agrade)
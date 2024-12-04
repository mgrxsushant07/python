names ={
    'Aryan': 50,
    "Aayush" : 75,
    "Ankit" :80,
    "Nischal":50,
    "Shudik" :70
}

scores={name: score for name,score in names.items() if score>=70}
print(f"High score is {scores}")
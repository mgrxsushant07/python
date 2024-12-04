#dictinarydict() Converts data to dictionary

places={
    'Kathmandu':['Swayambhunath Stupa (Monkey Temple)','Pashupatinath' ,'TempleBoudhanath', 'StupaKathmandu', 'Durbar SquareGarden of Dreams'],
    'Lumbini': ['Maya Devi Temple', 'Lumbini Garden', 'Ashokan Pillar', 'World Peace Pagoda', 'Lumbini Museum'],
    'Baglung': ['Rupse Waterfall', 'Dhorpatan Hunting Reserve', 'Baglung Kalika Temple', 'Bhairabsthan Temple', 'Bungdi Waterfall'],
    'Pokhara' :['Phewa Lake', 'Sarangkot', 'Devi’s Fall', 'World Peace Pagoda', 'Gupteshwor Cave']
}

place_name = input('Enter district name where u want to visit :').strip().lower()

is_avaiable= place_name in places

if is_avaiable:
    print('address found')
    print(f'The visiting places at {place_name} are :')
    
    for place in places[place_name]:
        print(place)

else:
    print("The palce u are searching is not found. sorry.....!")



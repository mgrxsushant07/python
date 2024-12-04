places = {
    'Kathmandu': ['Swayambhunath Stupa (Monkey Temple)', 'Pashupatinath Temple', 'Boudhanath Stupa', 'Kathmandu Durbar Square', 'Garden of Dreams'],
    'Lumbini': ['Maya Devi Temple', 'Lumbini Garden', 'Ashokan Pillar', 'World Peace Pagoda', 'Lumbini Museum'],
    'Baglung': ['Rupse Waterfall', 'Dhorpatan Hunting Reserve', 'Baglung Kalika Temple', 'Bhairabsthan Temple', 'Bungdi Waterfall'],
    'Pokhara': ['Phewa Lake', 'Sarangkot', 'Devi’s Fall', 'World Peace Pagoda', 'Gupteshwor Cave']
}

place_name = input('Enter district name where you want to visit: ').strip().lower()  # Convert input to lowercase and strip any extra spaces

# Convert dictionary keys to lowercase for comparison
places_lower = {key.lower(): value for key, value in places.items()}

is_available = place_name in places_lower

if is_available:
    print('Address found')
    print(f'The visiting places at {place_name.capitalize()} are:')
    
    for place in places_lower[place_name]:
        print(place)
else:
    print("The place you are searching is not found. Sorry.....!")

my_info={
    'Name': 'Sushant Gaha Magar',
    'Date_of_birth':'2007/12/26' ,
    'fav_game' :['football', 'cricket' , 'volleyball'],
    'address' : {
        "temp":"palpa",
        'parmanent':'sainamaina -1'
    }
}

my_info['Date_of_birth'] = '2008/12/26' #this statement is use if u want to change the date_of_birth 
my_info['fav_game'][1] = 'tabletanis'

my_info['fav_music'] = ["Imagine" ,"Billie Jean","I Will Always Love You","My Heart Will Go On" ]

print(my_info['Name'])
print(my_info['Date_of_birth'])
print(my_info['fav_game'][1])
print(", ".join(my_info['fav_game']))
print(my_info['address']['parmanent'])
print(", ".join(my_info['fav_music']))


print
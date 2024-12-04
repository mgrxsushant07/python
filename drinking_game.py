# Apta Apta Game Rules:
#  1. Players stack their hands on top of each other in a pile.
#  2. The leader calls out a number (target number).
#  3. Starting from the bottom, players remove their hands one by one while counting out loud.
#  4. When the count reaches the target number, the player whose hand is on top at that moment has to drink.
#  5. The game continues with the previous round's loser as the new leader.

# Algorithm:
# step 1: Input desired number(n) of players by the user
# step 2: Create player 1, player 2, player 3, .... player n
# step 3: Print("Apta Apta, Apta Apta, your favourite game, game start!")
# step 4: Pick a random player from the list and mark it as a Leader
# step 5: Ask the leader to enter a random number (int, whole number)
# step 6: Count up to the entered number by the Leader and select users randomly and assign the number
# step 7: The user who was selected randomly at the number entered by the leader has to drink.
# step 8: Pring "Drink!!! player number"
# step 9: Leader = player selected in step 7
# step 10: Ask the user if they want to continue the game
# step 10: If yes, Goto step 5 else end the game

import random
# Taking input from user for the number of players
player_number = int(input("please enter number of players: "))

# List for storing players
# players = []

# # creating players and storing in a list
# for i in range (player_number):
#     players.append(f"Player {i+1}")

# Using tuple to store the list of players
players = tuple(f"Player {i+1}" for i in range(player_number))

print(f"list of players : {players}")

# Selecting random player as a leader
leader = random.choice(players)

# Looping the game untill the player wants to play
while True:
    print (f"{leader} is the leader")

    # Asking leader to call a number
    target_number = int(input (f"{leader}, please call a number: "))

    # Counting upto the target number and randomly selecting players in each count
    count = 1
    current_player = "jondoe"
    while count <= target_number:
        apt = random.choice(players)
        if current_player != apt:
            if count != target_number:
                print (f"{apt }: {count}")
            else:
                print (f"{apt} : Drink!!!!")
                leader = apt
            count +=1
            current_player = apt

    # Ask if the user wants to continue or quit 
    continue_game = input("Do you want to play another round? (yes/no): ").strip().lower() 
    if continue_game != 'yes': 
        print("Thanks for playing! Goodbye.") 
        break
    print (f"{leader} is the new Leader!!")
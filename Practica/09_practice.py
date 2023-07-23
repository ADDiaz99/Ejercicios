"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
"""

print("*" * 50)
print("         WELCOME TO ROCK, PAPER, SCISSORS!")
print("*" * 50)


game_state = True
player_1_points = 0
player_2_points = 0

while game_state:
    
    print(f"PLAYER 1 POINTS: {player_1_points}" + f"       PLAYER 2 POINTS: {player_2_points}")
    if player_1_points >= 3: 
        print("Player 1 Wins the game, Congratulations!")
        game_state = False
        break
    if player_2_points >= 3: 
        print("Player 2 Wins the game, Congratulations!")
        game_state = False
        break

    player_1_input = input("\nPlayer 1, choose! --> ")
    player_2_input = input("\nNow, Player 2, choose! --> ")

    if player_1_input == 'rock' and player_2_input == 'scissors':
        print("player 1 wins the round!")
        player_1_points += 1
    elif player_1_input == 'rock' and player_2_input == 'rock':
        print("Tie!")
    elif player_1_input == 'rock' and player_2_input == 'paper':
        print("Player 2 wins the round!")
        player_2_points += 1
    
    if player_1_input == 'scissors' and player_2_input == 'paper':
        print("player 1 wins the round!")
        player_1_points += 1
    elif player_1_input == 'scissors' and player_2_input == 'scissors':
        print("Tie!")
    elif player_1_input == 'scissors' and player_2_input == 'rock':
        print("Player 2 wins the round!")
        player_2_points += 1
    
    if player_1_input == 'paper' and player_2_input == 'rock':
        print("player 1 wins the round!")
        player_1_points += 1
    elif player_1_input == 'paper' and player_2_input == 'paper':
        print("Tie!")
    elif player_1_input == 'paper' and player_2_input == 'scissors':
        print("Player 2 wins the round!")
        player_2_points += 1

        
#player_1_input = input("")
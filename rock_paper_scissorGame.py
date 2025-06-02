import random

game_type = int(input("Press 1 to play with computer & 2 to play with friend: "))

def play_type(type):
    if type == 1:
        player1 = input('Rock:(R) Paper:(P) Scissors:(S)').upper()
        player2 = random.choice(['R', 'P', 'S'])
        print(f"Computer chose {player2}")
        return player1, player2
    else:
        player1 = input('Rock:(R) Paper:(P) Scissors:(S)').upper()
        player2 = input('Rock:(R) Paper:(P) Scissors:(S)').upper()
        return player1, player2

def game_rule(player1, player2):
    if player1 == player2:
        result = "Tie"
    elif (player1 == 'R' and player2 == 'S') or (player1 == 'P' and player2 == 'R') or (player1 == 'S' and player2 == 'P'):
        result = f"{player1} wins against {player2}"
    else:
        result = f"{player1} loses against {player2}"
    
    print(result)

while True:
    player1, player2 = play_type(game_type)
    game_rule(player1, player2)
    play_again = input("Play again? (Y/N): ").upper()
    if play_again != "Y":
        break
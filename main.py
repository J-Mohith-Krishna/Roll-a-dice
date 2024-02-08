import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_score = roll_dice() + roll_dice()
    computer_score = roll_dice() + roll_dice()
    
    print("Player's score:", player_score)
    print("Computer's score:", computer_score)
    
    if player_score > computer_score:
        print("Congratulations! You win!")
    elif player_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

play_game()

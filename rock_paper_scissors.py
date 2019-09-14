import random

choices = ['rock', 'paper', 'scissors']
player_points = 0
computer_points = 0

while player_points < 3 and computer_points < 3:
    player_choice = input('Choose rock, paper or scissors: ')
    player_choice = player_choice.lower()
    while player_choice not in choices:
        player_choice = input('Choose rock, paper or scissors: ')

    computer_choice = random.choice(choices)
    print('Computer chose', computer_choice)

    if (player_choice == 'rock' and computer_choice == 'scissors' or
        player_choice == 'paper' and computer_choice == 'rock' or
        player_choice == 'scissors' and computer_choice == 'paper'):
            player_points = player_points + 1
            print('Player wins the round.')
    elif player_choice == computer_choice:
        print('It\'s a draw')
    else:
        computer_points = computer_points + 1
        print('Computer wins the round.')

    print('Score - Player:', player_points, 'Computer:', computer_points)

if player_points == 3:
    print('Player wins the game.')
else:
    print('Computer wins the game.')







    

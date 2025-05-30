import random
choices = ["rock", "paper", "scissors"]
print('Lets play rock, paper or scissors!')
player_wins = 0
computer_wins = 0
while player_wins < 2 and computer_wins < 2:
  player_choice = input('Choose your move: ').lower()
  computer_choice = random.choice(choices)
  print(f'Computer chose: {computer_choice}')
  if (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock'):
    winner = 'Player'
  elif player_choice == computer_choice:
    winner = 'Tie'
  else:
    winner = 'Computer'
  if winner == 'Player':
    print('You Won')
  elif winner == 'Computer':
    print('Computer won')
  else:
    print('Its a tie')
  if winner == 'Player':
    player_wins += 1
  elif winner == 'Computer':
    computer_wins += 1
  print(f'Current Score - Player: {player_wins}')
  print(f'Computer: {computer_wins}')

if player_wins > computer_wins:
  print('Congratulations! You won.')
else:
  print('Computer won!')
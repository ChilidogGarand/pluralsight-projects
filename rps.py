import random
computer_choice = random.choice(['scissors', 'rock', 'paper'])
user_choice = input('Choose your weapon: rock, paper, or scissors?\n')
if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('Winner winner, chicken dinner!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Winner winner, chicken dinner!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('Winner winner, chicken dinner!')
else:
    print('You lost, you big freaking loser. The computer chose ' + str(computer_choice) + '. You got beat by a rock we tricked into thinking. Go home and think about your life choices.')
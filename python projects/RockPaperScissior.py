import random
print('Rock Paper Scissior Game! \n' + 
        'Game Rules \n' +
        'Rock vs Paper --> Paper wins \n' +
        'Rock vs Scissior --> Rock wins \n' +
        'Paper vs Scissor --> Scissor wins \n')
while True:
    print('Enter your choice: Rock, Paper, Scissior')
    user_choice = input().lower()
    choices = ['rock', 'paper', 'scissior']
    computer_choice = random.choice(choices)
    print('Computer choice: ' + computer_choice)
    if user_choice not in choices:
        print('Invalid choice. Please enter a valid choice')
        continue
    if user_choice == computer_choice:
        print('It is a tie')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('Computer wins')
        else:
            print('You win')
    elif user_choice == 'paper':
        if computer_choice == 'scissior':
            print('Computer wins')
        else:
            print('You win')
    elif user_choice == 'scissior':
        if computer_choice == 'rock':
            print('Computer wins')
        else:
            print('You win')
    print('Do you want to play again? (yes or no)')
    play_again = input().lower()
    if play_again != 'yes':
        break
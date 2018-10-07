# Import functions
import random
import dice

# Randomly generate the roll of five dice
die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)
die4 = random.randint(1,6)
die5 = random.randint(1,6)

# Define the correct score
score = 0

if die1 == 3:
    score += 2

if die2 == 3:
    score += 2

if die3 == 3:
    score += 2

if die4 == 3:
    score += 2

if die5 == 3:
    score += 2


if die1 == 5:
    score += 4

if die2 == 5:
    score += 4

if die3 == 5:
    score += 4

if die4 == 5:
    score += 4

if die5 == 5:
    score += 4

# Ask the user if he/she want to play
play_game = input('would you like to play Petals around the Rose [y|n]? ')

# Display dice roll and ask the user for a guess
if play_game == 'y':
    dice.display_dice(die1, die2, die3, die4, die5)
    guess = int(input('Please enter your guess for the roll: '))

# Display the result of guess
if guess == score:
    print('Well done! You guessed it!')
elif guess % 2 == 0:
    print("No sorry, it's", score, "not", guess)
else:
    print("No sorry, it's ", score, " not ", guess, \
          ". The score is always even.", sep='')

# Ask the user if he/she want to play again
another_attempt = input('Roll dice again [y|n]? ')

# Loop
while another_attempt == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)
        die4 = random.randint(1,6)
        die5 = random.randint(1,6)
        dice.display_dice(die1, die2, die3, die4, die5)
        guess = int(input('Please enter your guess for the roll: '))
        if guess == score:
            print('Well done! You guessed it!')
        elif guess % 2 == 0:
            print("No sorry, it's", score, "not", guess)
        else:
            print("No sorry, it's ", score, " not ", guess, \
                  ". The score is always even.", sep='')
        # Update loop control
        another_attempt = input('Roll dice again [y|n]? ')

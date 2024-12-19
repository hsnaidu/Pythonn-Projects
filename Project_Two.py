import random

# Generate a random number
number = random.randint(1, 10)
guess = 0

# User Input
while True:
    guess_number = int(input('Enter a Number between 1 and 10: '))
    guess += 1  # Increment the guess counter
    
    if guess_number > number:
        print('Number is Greater!! Try again.')
    elif guess_number < number:
        print('Number is Lesser!! Try again.')
    else:
        print(f'You found the number {number} in {guess} guesses!')
        break

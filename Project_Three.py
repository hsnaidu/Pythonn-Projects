# Rock Paper Scissors Game

import random
chance  = 5

computer_play = {
    0 : 'Rock',
    1 : 'Paper',
    2 : 'Scissors'
}

human_play = {
    'Rock' : 0,
    'Paper' : 1,
    'Scissors' : 2
}

# LOGIC
# comp    human   human_score
# Rock -- Rock -- 0
# Rock -- Paper -- 1
# Rock -- Scissors -- 0
i = 0
for i in range(5):
    key = random.randint(0,2)
    human_key = input('Enter Rock, Paper, Scissors : ')
    print(computer_play[key])
    if computer_play[key] == human_play[human_key] :
        print('Draw')
        break
    else:
        print('processing')
    
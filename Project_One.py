# Quiz Game 

# Asking if user want's to play
play_time = input('Do you want to play the game {y/n}: ')

# List of question & answers 
question_key = ['1','2','3','4']
answer_key = ['one','two','three','four']

# Result 
result = {}

# User's Name
name = input('Enter your name : ')
result['Name'] = name

# Init Score
score = 0
result['Score'] = score

# Game 
if play_time == 'y': 
    for i in range(len(question_key)):
        print(f'Your Question : {question_key[i]}')
        answer = input('Enter your answer : ')
        
        if answer == answer_key[i]:
            result['Score'] += 1
        else:
            pass
    
    print(result)
    
    # Printing Final Result
    if result['Score'] <= 0:
        print('Better Luck Next Time {}'.format(result['Name']))
        # print(result)

else: 
    quit() # Default Python Function








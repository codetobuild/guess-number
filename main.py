import random

# guess number within range function
def computer_guess(low , high):

    feedback = ''
    print(f'\nNow, guess a number between {low} and {high}')

    status = input('Do you want to continue (y/n)?').lower()
    if(status == 'n'):
        return
    
    print('Computer guessing now.........\n')
    
    while feedback != 'c':
        if low != high:
              guess = random.randint(low, high)
        else:
            guess = low
       
        print(f'\nComputer guessed a number = {guess}')

        feedback = input(f'Is {guess} too high[H], too low[L] or correct[C] guessed number? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f'\nHurray! computer has guessed number {guess} correctly\n.')
    
    

# start game function
def gameStart():
    print('\nLet\'s play a guessing number game.\nThe rule is that you will guess a number between a range and computer will guess that number\n')

    status = input('Do you want to Play (y/n)?').lower()

    while(status == 'y'):
        low = int(input(f'\nEnter a starting guess number range:  '))
        high = int(input(f'Enter a end guess number range:  '))
        print(low, high)
        computer_guess(low, high)

        status = input('Do you want to play again? (y/n)?').lower()

gameStart()

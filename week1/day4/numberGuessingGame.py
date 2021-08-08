userGuess = ''

question = (
    'I am thinking of a number from 1-100 \nCan you guess the correct number?\n')

# In the below while and if statements, input the number you would like to have as your number to be guessed by the user
while userGuess != '48':
    userGuess = input(question)
    if userGuess < '48':
        print('Wrong number! Your guess was too low!\n')

    if userGuess > '48':
        print('Wrong number! Your guess was too high!\n')

    if userGuess == '48':
        print('You have guessed the correct number! Congratulations!')

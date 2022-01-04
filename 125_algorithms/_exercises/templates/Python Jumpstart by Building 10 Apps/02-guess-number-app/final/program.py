_______ r__

print('---------------------------------')
print('   GUESS THAT NUMBER GAME')
print('---------------------------------')
print()

the_number  r__.randint(0, 100)
guess  -1

name  input('Player what is your name? ')

w___ guess ! the_number:
    guess_text  input('Guess a number between 0 and 100: ')
    guess  i..(guess_text)

    __ guess < the_number:
        # print('Your guess of ' + guess + ' was too LOW.')
        print('Sorry {}, your guess of {} was too LOW.'.f..(name, guess))
    ____ guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.f..(name, guess))
    ____:
        print('Excellent work {}, you won, it was {}!'.f..(name, guess))

print('done')


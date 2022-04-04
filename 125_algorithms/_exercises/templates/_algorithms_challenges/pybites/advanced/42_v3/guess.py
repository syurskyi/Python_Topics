_______ r__

MAX_GUESSES = 5
START, END = 1, 20


___ get_random_number
    """Get a random number between START and END, returns int"""
    r.. r__.randint(START, END)


c_ Game:
    """Number guess class, make it callable to initiate game"""

    ___ -
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        _guesses = s..()
        _answer = get_random_number()
        _win = F..

    ___ guess
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        guess = input('Your guess: ')
        __ n.. guess:
            print('Please enter a number')
            r.. V...('Nothing entered')
        __ n.. a..(c.i.. ___ c __ s..(guess:
            print('Should be a number')
            r.. V...('Non-digit entered')
        guess = i..(guess)
        __ n.. (START <= guess <= END
            print('Number not in range')
            r.. V...('Out of range')
        __ guess __ _guesses:
            print('Already guessed')
            r.. V...('Retry previous guess')
        _guesses.add(guess)
        r.. guess

    ___ _validate_guess  guess
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        __ guess __ _answer:
            print _*{guess} is correct!')
            r.. T..
        ____ guess < _answer:
            print _*{guess} is too low')
        ____
            print _*{guess} is too high')
        r.. F..

    ___ __call__
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        w.... l..(_guesses) < MAX_GUESSES a.. n.. _win:
            ___
                this_guess = guess()
            ______ V..
                _____
            __ _validate_guess(this_guess
                _win = T..
                r..
        print _*Guessed {MAX_GUESSES} times, answer was {_answer}')
        r..


__ _____ __ _____
    game = Game()
    game()

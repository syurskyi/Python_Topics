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
        
        w... T...
            ___
                number = input("Guess a number between 1 and 20: ")
                result = i..(number)
            ______:
                __ number __ N.. o. l..(number) __ 0:
                    print('Please enter a number')
                ____
                    print('Should be a number')
                r.. V...
            ____
                __ n.. START <= result <= END:
                    print('Number not in range')
                ____ result __ _guesses:
                    print('Already guessed')
                ____
                    _guesses.add(result)
                    r.. result
                r.. V...
             
            







    ___ _validate_guess  guess
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        
        correct = F..
        __ guess __ _answer:
            print(f"{guess} is correct!")
            correct = T..
        ____ guess > _answer:
            print(f"{guess} is too high")
        ____
            print(f"{guess} is too low")
        
        r.. correct
    ___ __call__
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""

        
        ___ i __ r..(1,MAX_GUESSES + 1
            w... T...
                ___
                    user_guess = guess()
                ______ V..
                    p..
                ____
                    _____

            
            _win = _validate_guess(user_guess)


            __ _win:
                _____


        __ _win:
            print(f"It took you {i} guesses")
        ____
            print(f"Guessed 5 times, answer was {_answer}")
            










__ _____ __ _____
    game = Game()
    game()

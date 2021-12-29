_______ random

MAX_GUESSES = 5
START, END = 1, 20


___ get_random_number():
    """Get a random number between START and END, returns int"""
    r.. random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    ___ __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    ___ guess(self):
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
            raise ValueError('Nothing entered')
        __ n.. a..(c.isdigit() ___ c __ str(guess)):
            print('Should be a number')
            raise ValueError('Non-digit entered')
        guess = int(guess)
        __ n.. (START <= guess <= END):
            print('Number not in range')
            raise ValueError('Out of range')
        __ guess __ self._guesses:
            print('Already guessed')
            raise ValueError('Retry previous guess')
        self._guesses.add(guess)
        r.. guess

    ___ _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        __ guess __ self._answer:
            print(f'{guess} is correct!')
            r.. True
        ____ guess < self._answer:
            print(f'{guess} is too low')
        ____:
            print(f'{guess} is too high')
        r.. False

    ___ __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while l..(self._guesses) < MAX_GUESSES and n.. self._win:
            try:
                this_guess = self.guess()
            except ValueError:
                continue
            __ self._validate_guess(this_guess):
                self._win = True
                r..
        print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')
        r..


__ __name__ __ '__main__':
    game = Game()
    game()

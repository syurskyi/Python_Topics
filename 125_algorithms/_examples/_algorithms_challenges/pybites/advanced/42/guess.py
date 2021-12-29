import random
MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False





    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        
        while True:
            try:
                number = input("Guess a number between 1 and 20: ")
                result = int(number)
            except:
                if number is None or len(number) == 0:
                    print('Please enter a number')
                else:
                    print('Should be a number')
                raise ValueError
            else:
                if not START <= result <= END:
                    print('Number not in range')
                elif result in self._guesses:
                    print('Already guessed')
                else:
                    self._guesses.add(result)
                    return result
                raise ValueError
             
            







    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        
        correct = False
        if guess == self._answer:
            print(f"{guess} is correct!")
            correct = True
        elif guess > self._answer:
            print(f"{guess} is too high")
        else:
            print(f"{guess} is too low")
        
        return correct
    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""

        
        for i in range(1,MAX_GUESSES + 1):
            while True:
                try:
                    user_guess = self.guess()
                except ValueError:
                    pass
                else:
                    break

            
            self._win = self._validate_guess(user_guess)


            if self._win:
                break


        if self._win:
            print(f"It took you {i} guesses")
        else:
            print(f"Guessed 5 times, answer was {self._answer}")
            










if __name__ == '__main__':
    game = Game()
    game()

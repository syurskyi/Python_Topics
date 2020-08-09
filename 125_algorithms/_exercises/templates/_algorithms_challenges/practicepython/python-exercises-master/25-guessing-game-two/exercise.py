#! /Users/piotrjankiewicz/anaconda3/bin/python3.6

___ guess(options
    possible = options

    __ le.(possible) __ 1:
        print('The guess has to be: %s' % (possible[0]))
        r_

    index = int(le.(possible) / 2)
    currentGuess = possible[index]
    print('Computer guesses: %s' % currentGuess)
    feedback = input('To big ? (bigger) To small? (smaller) ? Good guess? (equal)\n')

    allowed = ['bigger', 'smaller', 'equal']

    __ feedback not in allowed:
        print('Uknown command :(')
        guess(possible)
    ____ feedback __ allowed[0]:
        __ currentGuess __ 100:
            print("Can't be bigger! It has to be %s" % currentGuess)
            r_
        guess(possible[index + 1:le.(possible)])
    ____ feedback __ allowed[1]:
        guess(possible[0:index])
    ____ feedback __ allowed[2]:
        print('Yes! I am a smart program!')
        r_


__ __name__ __ '__main__':
    guess(range(0, 101))

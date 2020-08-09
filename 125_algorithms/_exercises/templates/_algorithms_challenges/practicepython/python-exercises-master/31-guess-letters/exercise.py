#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ os
______ random
______ sys


___ getWord(
    cwd = os.getcwd()
    filePath = cwd + '/30-pick-word/sowpods.txt'
    with open(filePath, 'r') as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
        r_ word


class HangMan:

    ___ __init__(self, word
        self.word = word
        self.state = []
        self.generateState()
        self.guessCount = 0
        self.welcome()
        self.startGame()

    ___ generateState(self
        ___ char in self.word:
            self.state.append('_')

    ___ startGame(self
        guess = self.askForGuess()
        self.checkGuess(guess)
        self.goOn()

    ___ welcome(self
        print('''
                                                
  /\  /\__ _ _ __   __ _    /\/\   __ _ _ __  
 / /_/ / _` | '_ \ / _` |  /    \ / _` | '_ \ 
/ __  / (_| | | | | (_| | / /\/\ \ (_| | | | |
\/ /_/ \__,_|_| |_|\__, | \/    \/\__,_|_| |_|
                   |___/                               
        
            Guess The word!
            
        ''')

    ___ askForGuess(self
        guess = str(input('Guess a latter: ')).upper()
        self.guessCount += 1
        r_ guess

    ___ checkGuess(self, guess
        countCorrect = 0
        ___ index, value in enumerate(self.word
            __ guess __ value:
                self.state[index] = value
                countCorrect += 1
        __ countCorrect != 0:
            print('You guessed!')
        ____
            print('Try again!')

    ___ goOn(self
        self.displayState()
        guess = self.askForGuess()
        self.checkGuess(guess)
        self.checkIfWon()
        self.goOn()

    ___ displayState(self
        ___ char in self.state:
            print(char, end='')
        print('\n')

    ___ checkIfWon(self
        countCorrect = 0
        ___ index, value in enumerate(self.state
            __ value __ self.word[index]:
                countCorrect += 1
        __ countCorrect __ le.(self.word
            sys.exit('You won!')


__ __name__ __ '__main__':
    word = getWord()
    print(word)
    game = HangMan(word)

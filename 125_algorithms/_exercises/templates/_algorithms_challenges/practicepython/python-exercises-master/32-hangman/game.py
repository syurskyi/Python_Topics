______ sys
______ os

class HangMan:

    ___ __init__(self, word, hangmans
        os.system('clear')
        self.hangmans = hangmans
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
        self.displayHangman()
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
        Press any key To Start
            
        ''')
        input()
        os.system('clear')

    ___ displayHangman(self
        print(self.hangmans[self.guessCount])


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
        os.system('clear')
        self.displayHangman()
        self.displayState()
        guess = self.askForGuess()
        self.checkGuess(guess)
        self.checkIfWon()
        self.goOn()

    ___ displayState(self
        ___ char in self.state:
            print(" " + char + " ", end='')
        print('\n')

    ___ checkIfWon(self
        __ self.guessCount __ 6:
            sys.exit('You lose! The right word was: ' + self.word)
        countCorrect = 0
        ___ index, value in enumerate(self.state
            __ value __ self.word[index]:
                countCorrect += 1
        __ countCorrect __ le.(self.word
            sys.exit('You won!')
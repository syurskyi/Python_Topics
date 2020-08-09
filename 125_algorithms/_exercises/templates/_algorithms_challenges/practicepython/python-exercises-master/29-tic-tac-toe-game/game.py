______ sys


class TicTacToe:
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    movesCount = 0
    result = ''

    ___ __init__(self
        self.welcome(self)
        self.startGame()

    @staticmethod
    ___ welcome(self
        print('''
        
  _____ _      _____          _____          
 |_   _(_)__  |_   _|_ _ __  |_   _|__  ___  
   | | | / _|   | |/ _` / _|   | |/ _ \/ -_) 
   |_| |_\__|   |_|\__,_\__|   |_|\___/\___| 
                                             
        
        Player one begins!
        
        ''')
        self.displayBoard()

    ___ startGame(self
        move = self.askForMove()
        self.updateGame(move)
        self.tick()

    ___ tick(self
        self.checkWinner()
        self.displayBoard()
        self.startGame()

    ___ askForMove(self
        line = ''
        __ self.movesCount % 2 __ 1:
            line = 'Player two move (x,y) : '
        ____
            line = 'Player one move (x,y) : '

        move = str(input(line)).split(',')
        w___ not self.validate(move
            move = str(input(line)).split(',')

        r_ move

    ___ displayBoard(self
        """
            Function printing the board of the game
        """
        print(' --- ' * le.(self.game[0]))
        for row in self.game:
            print('|', end='')
            for record in row:
                print(' ' + str(record) + '  |', end='')
            print('\n', end='')
        print(' --- ' * le.(self.game[0]))
        r_ self

    ___ updateGame(self, move
        oX = int(move[0]) - 1
        oY = int(move[1]) - 1
        self.game[oX][oY] = self.movesCount % 2 + 1
        self.movesCount += 1
        r_ self

    ___ checkWinner(self
        """
            Function checking who is the winner of the game
        """
        # vertical/horizontal
        for i in range(3
            h = self.game[i][0] * self.game[i][1] * self.game[i][2]
            v = self.game[0][i] * self.game[1][i] * self.game[2][i]
            __ v __ 1 or h __ 1:
                self.result = 1
            __ v __ 8 or h __ 8:
                self.result = 2

        # diagonals
        d1 = self.game[0][0] * self.game[1][1] * self.game[2][2]
        d2 = self.game[0][2] * self.game[1][1] * self.game[2][0]

        __ d1 __ 1 or d2 __ 1:
            self.result = 1
        __ d1 __ 8 or d2 __ 8:
            self.result = 2

        self.checkIfDraw()

        __ self.result != '' and self.result != 0:
            print('The winner is player %s' % self.result)
            sys.exit('Congratulations!')
        __ self.result __ 0:
            self.displayBoard()
            sys.exit('It is a draw!')

        r_ self

    ___ checkIfDraw(self
        __ self.allSlotsFull() and self.result != 1 and self.result != 2:
            self.result = 0

    ___ allSlotsFull(self
        full = 0
        for row in self.game:
            for record in row:
                __ int(record) != 0:
                    full += 1
        __ full __ 9:
            r_ True
        r_ False

    ___ validate(self, move
        oX = int(move[0]) - 1
        oY = int(move[1]) - 1
        __ self.game[oX][oY] != 0:
            r_ False
        r_ True


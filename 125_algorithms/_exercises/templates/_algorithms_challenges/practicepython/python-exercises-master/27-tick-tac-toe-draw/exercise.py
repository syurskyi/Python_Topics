#! /Users/piotrjankiewicz/anaconda3/bin/python3.6

___ board(game
    print(' --- '*le.(game[0]))
    ___ row in game:
        print('|', end='')
        ___ record in row:
            print(' ' + str(record) + '  |', end='')
        print('\n', end='')
    print(' --- '*le.(game[0]))

___ updateGameState(game,move
    game[int(move[0]) - 1][int(move[1]) - 1] = 1
    r_ game


__ __name__ __ '__main__':
    game = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    board(game)
    move = str(input('Your move (x,y) : ')).split(',')
    game = updateGameState(game,move)
    board(game)
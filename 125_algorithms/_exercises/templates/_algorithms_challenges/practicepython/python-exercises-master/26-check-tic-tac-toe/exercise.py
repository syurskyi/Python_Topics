#! /Users/piotrjankiewicz/anaconda3/bin/python3.6


___ ticTacToe(game
    # vertical/horizontal
    for i in range(3
        h = game[i][0] * game[i][0] * game[i][0]
        v = game[0][i] * game[1][i] * game[2][i]
        __ v __ 1 or h __ 1:
            r_ 1
        __ v __ 8 or h __ 8:
            r_ 2
    # diagonals

    d1 = game[0][0] * game[1][1] * game[2][2]
    d2 = game[0][2] * game[1][1] * game[2][0]

    __ d1 __ 1 or d2 __ 1:
        r_ 1
    __ d1 __ 8 or d2 __ 8:
        r_ 2

    r_ 0


winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

__ __name__ __ '__main__':
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    print('The sample game:\n')

    for i in range(3
        print(str(game[i]) + '\n')

    winner = ticTacToe(game)

    print('The sample game winner is player: %s\n' % winner)

    print('Tests: \n')
    print('Assert "2" --> %s\n'%ticTacToe(winner_is_2))
    print('Assert "1" --> %s\n'%ticTacToe(winner_is_1))
    print('Assert "1" --> %s\n'%ticTacToe(winner_is_also_1))
    print('Assert "0" --> %s\n'%ticTacToe(no_winner))
    print('Assert "0" --> %s\n'%ticTacToe(also_no_winner))

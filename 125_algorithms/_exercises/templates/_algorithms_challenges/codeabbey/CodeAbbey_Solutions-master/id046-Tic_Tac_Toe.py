# Python 2.7

player_one = 'X'
player_two = 'O'
answer    # list

___ has_the_moves(player, moves):
    __ l..(moves) <= 2:
        r.. N..

    # Winning combinations
    win1 = (0,3,6) #[1,4,7]
    win2 = (1,4,7) #[2,5,8]
    win3 = (2,5,8) #[3,6,9]
    win4 = (0,4,8) #[1,5,9]
    win5 = (6,7,8) #[7,8,9]
    win6 = (3,4,5) #[4,5,6]
    win7 = (0,1,2) #[1,2,3]
    win8 = (6,7,8) #[7,8,9]
    winning_grids = [win1, win2, win3, win4, win5, win6, win7, win8]

    tried = [set(posibility) <= set(moves) ___ posibility __ winning_grids]
    r.. player __ any(tried) ____ N..

___ is_winner(board):
    # Check for winner
    player_one_moves = [i ___ i, x __ e..(board) __ x __ player_one]
    player_two_moves = [i ___ i, x __ e..(board) __ x __ player_two]

    player_one_won = has_the_moves(player_one, player_one_moves)
    player_two_won = has_the_moves(player_two, player_two_moves)

    __ player_one_won o. player_two_won:
        r.. True
    ____:
        r.. N..

___ tic_tac_toe(games):
    ___ game __ r..(games):
        board = [s..(x) ___ x __ r..(1, 10)] # Create the 3x3 Tic-Tac-Toe board.
        moves = [int(x) ___ x __ raw_input().s.. ] # Logs all player moves.

        ___ turn, move __ e..(moves):
            # Take turns rewriting the default board to player 1's X
            # and then player 2's O.
            board[move - 1] = player_one __ turn % 2 __ 0 ____ player_two

            __ is_winner(board):
                answer.a..(s..(turn+1))
                break; # Stops loop each time an answer is found.
            __ turn __ l..(moves) - 1:
                answer.a..('0') # Tie game

__ __name__ __ '__main__':
    tic_tac_toe(input())
    print(' '.join(answer))

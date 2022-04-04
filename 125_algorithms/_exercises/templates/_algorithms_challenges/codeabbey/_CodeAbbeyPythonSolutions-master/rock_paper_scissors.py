amount_values = i..(input
results    # list

___ get_round_winner(player1, player2
    player1_move = o..(player1)
    player2_move = o..(player2)
    __(player1_move < player2_move
        __(player1_move - player2_move < -2
            r.. 2
        r.. 1
    ____(player1_move > player2_move
        __(player1_move - player2_move > 2
            r.. 1
        r.. 2
    ____:
        r.. 0


___ get_match_winner(moves
    player_1_result = 0
    player_2_result = 0
    ___ i __ moves:
        round_winner = get_round_winner(i[0], i[1])
        __(round_winner __ 1
            player_1_result += 1
        ____(round_winner __ 2
            player_2_result += 1

    __(player_1_result > player_2_result
        r.. 1
    ____(player_2_result > player_1_result
        r.. 2
    ____:
        r.. 0
    
___ i __ r..(amount_values
    moves = l.. m..(s.., input().s..()))
    results.a..(get_match_winner(moves

print(*results)
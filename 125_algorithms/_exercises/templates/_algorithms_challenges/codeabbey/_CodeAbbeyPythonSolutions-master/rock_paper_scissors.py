amount_values = int(input())
results = []

___ get_round_winner(player1, player2
    player1_move = ord(player1)
    player2_move = ord(player2)
    __(player1_move < player2_move
        __(player1_move - player2_move < -2
            r_ 2
        r_ 1
    ____(player1_move > player2_move
        __(player1_move - player2_move > 2
            r_ 1
        r_ 2
    ____
        r_ 0


___ get_match_winner(moves
    player_1_result = 0
    player_2_result = 0
    for i in moves:
        round_winner = get_round_winner(i[0], i[1])
        __(round_winner __ 1
            player_1_result += 1
        ____(round_winner __ 2
            player_2_result += 1

    __(player_1_result > player_2_result
        r_ 1
    ____(player_2_result > player_1_result
        r_ 2
    ____
        r_ 0
    
for i in range(amount_values
    moves = list(map(str, input().split()))
    results.append(get_match_winner(moves))

print(*results)
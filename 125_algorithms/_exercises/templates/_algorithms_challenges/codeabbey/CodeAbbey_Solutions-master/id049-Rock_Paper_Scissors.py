___ playRPS(games
    answer = []
    ___ game in range(games
        matches = raw_input().split()
        player1,player2 = 0,0
        ___ match in matches:
            __ any(match __ x ___ x in ['RR','PP','SS']
                0
            ____ any(match __ x ___ x in ['RS','PR','SP']
                player1 += 1
            ____
                player2 += 1
        __ player1 > player2:
            answer.append("1")
        ____
            answer.append("2")
    print(' '.join(answer))
playRPS(input())

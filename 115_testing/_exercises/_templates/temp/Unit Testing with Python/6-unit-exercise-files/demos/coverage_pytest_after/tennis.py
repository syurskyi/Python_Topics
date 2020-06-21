___ tennis_score(p1points, p2points
    game _ TennisGame("Player 1", "Player 2")
    game.p1points _ p1points
    game.p2points _ p2points
    r_ game.score()

c_ TennisGame:

    ___  -   player1Name, player2Name
        player1Name _ player1Name
        player2Name _ player2Name
        p1points _ 0
        p2points _ 0
    
    ___ score
        result _ ""
        tempScore_0
        __ (p1points__p2points
            result _ {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(p1points, "Deuce")
        elif (p1points>_4 o. p2points>_4
            minusResult _ p1points-p2points
            __ (minusResult__1
                result _"Advantage " + player1Name
            elif (minusResult __-1
                result _"Advantage " + player2Name
            elif (minusResult>_2
                result _ "Win for " + player1Name
            ____:
                result _"Win for " + player2Name
        ____:
            ___ i __ ra..(1,3
                __ (i__1
                    tempScore _ p1points
                ____:
                    result+_"-"
                    tempScore _ p2points
                result +_ {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        r_ result

        ___ won_point  playerName # pragma: no cover
            __ playerName __ player1Name:
                p1points +_ 1
            ____:
                p2points +_ 1

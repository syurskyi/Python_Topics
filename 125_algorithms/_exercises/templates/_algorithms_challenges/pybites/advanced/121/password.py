_______ __


___ password_complexity(password
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score 0
    __ l.. ? >_ 8:
        score += 1
        first_eight password[:8]
        __ n.. __.s.. _ (.)\1',password
            score += 1

    



    __ __.s.. _ [a-z]',password) a.. __.s.. _ [A-Z]',password
        score += 1
    
    __ __.s.. _ [^\sa-zA-Z0-9]',password
        score += 1


    __ __.s.. _ \d',password) a.. __.s.. _ [a-zA-Z]',password
        score += 1


    r.. score

__ _______ __ _______
    password '123$Abc1'

    password_complexity ?



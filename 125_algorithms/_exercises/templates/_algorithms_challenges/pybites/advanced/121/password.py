_______ re


___ password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    __ l..(password) >= 8:
        score += 1
        first_eight = password[:8]
        __ n.. re.search(r'(.)\1',password):
            score += 1

    



    __ re.search(r'[a-z]',password) and re.search(r'[A-Z]',password):
        score += 1
    
    __ re.search(r'[^\sa-zA-Z0-9]',password):
        score += 1


    __ re.search(r'\d',password) and re.search(r'[a-zA-Z]',password):
        score += 1


    r.. score

__ __name__ __ "__main__":
    password = '123$Abc1'

    password_complexity(password)



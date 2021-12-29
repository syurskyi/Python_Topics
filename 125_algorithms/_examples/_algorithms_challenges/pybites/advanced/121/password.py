import re


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    if len(password) >= 8:
        score += 1
        first_eight = password[:8]
        if not re.search(r'(.)\1',password):
            score += 1

    



    if re.search(r'[a-z]',password) and re.search(r'[A-Z]',password):
        score += 1
    
    if re.search(r'[^\sa-zA-Z0-9]',password):
        score += 1


    if re.search(r'\d',password) and re.search(r'[a-zA-Z]',password):
        score += 1


    return score

if __name__ == "__main__":
    password = '123$Abc1'

    password_complexity(password)



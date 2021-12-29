scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    print(user_score)
    for index, score in enumerate(scores):
        if user_score < scores[0]:
            return None
        elif user_score < score:
            return belts[index-1]
    return belts[len(belts)-1]




print(get_belt(10))
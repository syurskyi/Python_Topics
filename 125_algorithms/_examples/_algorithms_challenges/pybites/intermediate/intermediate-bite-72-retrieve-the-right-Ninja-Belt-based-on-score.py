
scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    result = []
    for index, i in enumerate(scores):
        if index == 0:
            for j in range(0, i):
                result.insert(j, None)
            last = i
        else:
            for j in range(last, i):
                result.insert(j, belts[index - 1])
            last = i
    if user_score >= scores[len(scores)-1]:
        return belts[len(belts)-1]
    else:
        return result[user_score]

print(get_belt(1000, scores, belts))




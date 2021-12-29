scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    for score, belt in zip(scores[::-1], belts[::-1]):
        print(score)




print(scores[::-1])
get_belt(100)
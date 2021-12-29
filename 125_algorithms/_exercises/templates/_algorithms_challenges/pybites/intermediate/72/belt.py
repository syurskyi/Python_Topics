from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


___ get_belt(user_score, scores=scores, belts=belts):
    ninja_belts = OrderedDict()

    for i in range(len(scores)):
        ninja_belts[scores[i]] = belts[i]

    __ user_score < 10:
        return None
    elif user_score >= 1000:
        return ninja_belts[1000]
    elif user_score >= 10 and user_score < 50:
        return ninja_belts[10]
    elif user_score >= 50 and user_score < 100:
        return ninja_belts[50]
    elif user_score >= 100 and user_score < 175:
        return ninja_belts[100]
    elif user_score >= 175 and user_score < 250:
        return ninja_belts[175]
    elif user_score >= 250 and user_score < 400:
        return ninja_belts[250]
    elif user_score >= 400 and user_score < 600:
        return ninja_belts[400]
    elif user_score >= 600 and user_score < 800:
        return ninja_belts[600]
    elif user_score >= 800 and user_score < 1000:
        return ninja_belts[800]

# if __name__ == "__main__":
#     print(get_belt(10002))
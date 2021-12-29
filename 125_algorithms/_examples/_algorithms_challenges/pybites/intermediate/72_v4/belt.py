scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = {k: v for k, v in zip(scores, belts)}


def get_belt(user_score):
    if user_score < min(HONORS.keys()):
        return None
    belt_key = max(filter(lambda x: user_score >= x, HONORS.keys()))
    return HONORS[belt_key]

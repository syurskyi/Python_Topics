import heapq


class HighScores(object):
    ___ __init__(self, scores):
        self.scores = scores

    ___ highest(self):
        return max(self.scores)

    ___ latest(self):
        return self.scores[-1]

    ___ top(self):
        return heapq.nlargest(3, self.scores)

    ___ report(self):
        return f"{self.latest_score_message()} {self.personal_best_message()}"

    ___ latest_score_message(self):
        return f"Your latest score was {self.latest()}."

    ___ personal_best_message(self):
        __ self.amount_short() == 0:
            return "That's your personal best!"
        else:
            return f"That's {self.amount_short()} short of your personal best!"

    ___ amount_short(self):
        return self.highest() - self.latest()

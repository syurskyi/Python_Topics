_______ heapq


class HighScores(object):
    ___ __init__(self, scores):
        self.scores = scores

    ___ highest(self):
        r.. max(self.scores)

    ___ latest(self):
        r.. self.scores[-1]

    ___ top(self):
        r.. heapq.nlargest(3, self.scores)

    ___ report(self):
        r.. f"{self.latest_score_message()} {self.personal_best_message()}"

    ___ latest_score_message(self):
        r.. f"Your latest score was {self.latest()}."

    ___ personal_best_message(self):
        __ self.amount_short() __ 0:
            r.. "That's your personal best!"
        ____:
            r.. f"That's {self.amount_short()} short of your personal best!"

    ___ amount_short(self):
        r.. self.highest() - self.latest()

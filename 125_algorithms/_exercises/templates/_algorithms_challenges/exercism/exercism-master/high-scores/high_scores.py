______ heapq


class HighScores(object
    ___ __init__(self, scores
        self.scores = scores

    ___ highest(self
        r_ max(self.scores)

    ___ latest(self
        r_ self.scores[-1]

    ___ top(self
        r_ heapq.nlargest(3, self.scores)

    ___ report(self
        r_ f"{self.latest_score_message()} {self.personal_best_message()}"

    ___ latest_score_message(self
        r_ f"Your latest score was {self.latest()}."

    ___ personal_best_message(self
        __ self.amount_short() __ 0:
            r_ "That's your personal best!"
        ____
            r_ f"That's {self.amount_short()} short of your personal best!"

    ___ amount_short(self
        r_ self.highest() - self.latest()

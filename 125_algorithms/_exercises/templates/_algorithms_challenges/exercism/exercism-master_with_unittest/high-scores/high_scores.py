_______ heapq


c_ HighScores(o..
    ___ - , scores
        scores = scores

    ___ highest
        r.. m..(scores)

    ___ latest
        r.. scores[-1]

    ___ top
        r.. heapq.nlargest(3, scores)

    ___ report
        r.. f"{latest_score_message()} {personal_best_message()}"

    ___ latest_score_message
        r.. f"Your latest score was {latest()}."

    ___ personal_best_message
        __ amount_short() __ 0:
            r.. "That's your personal best!"
        ____:
            r.. f"That's {amount_short()} short of your personal best!"

    ___ amount_short
        r.. highest() - latest()


from tennis import tennis_score
import pytest


examples = (("expected_score", "player1_points", "player2_points", "comment"), 
[
("Love-All", 0, 0, "early game, scores equal"),
("Fifteen-All", 1, 1, "early game, scores equal"),
("Thirty-All", 2, 2, "early game, scores equal"),
("Love-Fifteen", 0, 1, "early game, uneven scores"),
("Fifteen-Love", 1, 0, "early game, uneven scores"),
("Thirty-Fifteen", 2, 1, "early game, uneven scores"),
("Forty-Thirty", 3, 2, "early game, uneven scores"),
("Advantage Player 1", 4, 3, "endgame, with uneven scores"),
("Advantage Player 1", 23, 22, "endgame, with uneven scores"),
("Deuce", 3, 3, "endgame, with even scores"),
("Deuce", 4, 4, "endgame, with even scores"),
("Deuce", 14, 14, "endgame, with even scores"),
("Win for Player 1", 4, 0, "endgame, with winner"),
("Win for Player 2", 1, 4, "endgame, with winner"),
("Win for Player 1", 6, 4, "endgame, with winner"),
])
@pytest.mark.parametrize(*examples)
def test_tennis_scores(expected_score, player1_points, player2_points, comment):
    assert expected_score == tennis_score(player1_points, player2_points)


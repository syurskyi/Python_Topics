from score import Score


def test_enum_content():
    a__ list(Score) == [Score.BEGINNER, Score.INTERMEDIATE,
                           Score.ADVANCED, Score.CHEATED]


def test_equality_comparison():
    a__ Score.BEGINNER is Score.BEGINNER
    a__ Score.INTERMEDIATE is not Score.ADVANCED


def test_str_using_thumbsup():
    a__ str(Score.BEGINNER) == 'BEGINNER => 👍👍'
    a__ str(Score.INTERMEDIATE) == 'INTERMEDIATE => 👍👍👍'
    a__ str(Score.ADVANCED) == 'ADVANCED => 👍👍👍👍'
    a__ str(Score.CHEATED) == 'CHEATED => 👍'


def test_average():
    a__ Score.average() == 2.5
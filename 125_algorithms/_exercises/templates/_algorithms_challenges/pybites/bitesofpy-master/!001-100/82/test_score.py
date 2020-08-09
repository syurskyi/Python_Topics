from score ______ Score


___ test_enum_content(
    assert list(Score) __ [Score.BEGINNER, Score.INTERMEDIATE,
                           Score.ADVANCED, Score.CHEATED]


___ test_equality_comparison(
    assert Score.BEGINNER is Score.BEGINNER
    assert Score.INTERMEDIATE is not Score.ADVANCED


___ test_str_using_thumbsup(
    assert str(Score.BEGINNER) __ 'BEGINNER => 👍👍'
    assert str(Score.INTERMEDIATE) __ 'INTERMEDIATE => 👍👍👍'
    assert str(Score.ADVANCED) __ 'ADVANCED => 👍👍👍👍'
    assert str(Score.CHEATED) __ 'CHEATED => 👍'


___ test_average(
    assert Score.average() __ 2.5
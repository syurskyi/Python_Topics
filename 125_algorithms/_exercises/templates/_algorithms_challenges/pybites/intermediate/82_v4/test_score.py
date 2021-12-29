____ score _______ Score


___ test_enum_content():
    ... l..(Score) __ [Score.BEGINNER, Score.INTERMEDIATE,
                           Score.ADVANCED, Score.CHEATED]


___ test_equality_comparison():
    ... Score.BEGINNER __ Score.BEGINNER
    ... Score.INTERMEDIATE __ n.. Score.ADVANCED


___ test_str_using_thumbsup():
    ... str(Score.BEGINNER) __ 'BEGINNER => 👍👍'
    ... str(Score.INTERMEDIATE) __ 'INTERMEDIATE => 👍👍👍'
    ... str(Score.ADVANCED) __ 'ADVANCED => 👍👍👍👍'
    ... str(Score.CHEATED) __ 'CHEATED => 👍'


___ test_average():
    ... Score.average() __ 2.5
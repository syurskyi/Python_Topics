____ score _______ Score


___ test_enum_content
    ... l..(Score) __ [Score.BEGINNER, Score.INTERMEDIATE,
                           Score.ADVANCED, Score.CHEATED]


___ test_equality_comparison
    ... Score.BEGINNER __ Score.BEGINNER
    ... Score.INTERMEDIATE __ n.. Score.ADVANCED


___ test_str_using_thumbsup
    ... s..(Score.BEGINNER) __ 'BEGINNER => 👍👍'
    ... s..(Score.INTERMEDIATE) __ 'INTERMEDIATE => 👍👍👍'
    ... s..(Score.ADVANCED) __ 'ADVANCED => 👍👍👍👍'
    ... s..(Score.CHEATED) __ 'CHEATED => 👍'


___ test_average
    ... Score.average() __ 2.5
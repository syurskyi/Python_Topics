
c_ Employee

    ___ - , fname, lname, score) __ N..
        first fname.t..
        last lname.t..
        score score

    ___ full_name
        r.. _* first} {last}'


khoo Employee('sc', 'khoo', 250)

print(khoo.full_name
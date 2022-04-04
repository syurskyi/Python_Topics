"""
DATE: 05 Nov 2020
TASK DESCRIPTION:

Write a function that receives one or more sequences. The sequences are already defined for you.
The function should return a table (list of strings) where the columns are the sequences
(example below).

To keep it simple we work with equally sized sequences so you don't have to worry about
handling a missing value (you should end up with a grid of 6 rows x n columns).
There are some Pythonic idioms you can use here, hint: think of pants ;)

Example call (look at the tests for more detail):

>>> generate_table(names, aliases)
['Julian | Pythonista', 'Bob | Nerd', 'PyBites | Coder',
 'Dante | Pythonista', 'Martin | Nerd', 'Rodolfo | Coder']
Bonus: use a generator to build up the table rows.
"""

_______ r__

names = 'Julian Bob PyBites Dante Martin Rodolfo'.s..
aliases = 'Pythonista Nerd Coder'.s..  * 2
points = r__.sample(r..(81, 101), 6)
awake = [T.., F..] * 3
SEPARATOR = ' | '


### ----------- My solution ---------------------------

___ my_generate_table(*args
    l    # list
    result = z..(*args)
    ___ i __ result:
        s = ""
        ___ t __ i:
            __ s __ "":
                s = s..(t)
            ____
                s = s + " | " + s..(t)
        l.a..(s)
    r.. l

### ---------- PyBites original solution ---------------

___ pyb_generate_table(*sequences
    ___ seq __ z..(*sequences
        seq = [s..(val) ___ val __ seq]
        y.. SEPARATOR.j..(seq)
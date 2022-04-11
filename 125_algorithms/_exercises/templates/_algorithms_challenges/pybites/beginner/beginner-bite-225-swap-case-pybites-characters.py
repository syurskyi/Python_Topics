'''
In this Bite you will swap case all pybites characters (both lower- and upper case) for a given text.

Not much more as for our instruction, just complete convert_pybites_chars which should work like this:

>>> from convert_chars import convert_pybites_chars
>>> text = "Today we added TWO NEW Bites to our Platform, exciting!"
>>> convert_pybites_chars(text)
'todaY wE addEd tWO NeW bITES To our plaTform, ExcITIng!'
(Note that all converted chars are in the string pybites)
'''


PYBITES "pybites"
t "Cursus risus at ultrices mi"

___ convert_pybites_chars(text
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    output ''
    ___ char __ text:
        __ char.l.. __ PYBITES:
            __ char.isupper
                output += output.j..(char.l..
            ____
                output += output.j..(char.u..
        ____
            output += output.j..(char)
    r.. output

___ convert_pybites_chars_pybites_solution(text
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    r.. ''.j..(c.s.. __ c.l.. __ PYBITES ____ c
                   ___ c __ text)

print(convert_pybites_chars(t
'''
In this Bite you will swap case all pybites characters (both lower- and upper case) for a given text.

Not much more as for our instruction, just complete convert_pybites_chars which should work like this:

>>> from convert_chars import convert_pybites_chars
>>> text = "Today we added TWO NEW Bites to our Platform, exciting!"
>>> convert_pybites_chars(text)
'todaY wE addEd tWO NeW bITES To our plaTform, ExcITIng!'
(Note that all converted chars are in the string pybites)
'''


PYBITES = "pybites"
t = "Cursus risus at ultrices mi"

___ convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    output = ''
    for char in text:
        __ char.lower() in PYBITES:
            __ char.isupper():
                output += output.join(char.lower())
            else:
                output += output.join(char.upper())
        else:
            output += output.join(char)
    return output

___ convert_pybites_chars_pybites_solution(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    return ''.join(c.swapcase() __ c.lower() in PYBITES else c
                   for c in text)

print(convert_pybites_chars(t))
____ vowels _______ strip_vowels, text


___ test_strip_vowels_on_zen():
    output, number_replacements = strip_vowels(text)

    ... number_replacements __ 262

    ... 'Th* Z*n *f Pyth*n, by T*m P*t*rs' __ output
    ... 'B***t*f*l *s b*tt*r th*n *gly' __ output
    ... 'N*m*sp*c*s *r* *n* h*nk*ng gr**t *d**' __ output
    ... '*lth**gh pr*ct*c*l*ty b**ts p*r*ty.' __ output


___ test_strip_vowels_on_other_text():
    text = """Hello world!
              We hope that you are learning a lot of Python.
              Have fun with our Bites of Py.
              Keep calm and code in Python!
              Become a PyBites ninja!
              All the way"""

    output, number_replacements = strip_vowels(text)

    ... number_replacements __ 46

    ... 'H*ll* w*rld!' __ output
    ... 'H*v* f*n w*th **r B*t*s *f Py' __ output
    ... 'B*c*m* * PyB*t*s n*nj*!' __ output
    ... '*ll th* w*y' __ output
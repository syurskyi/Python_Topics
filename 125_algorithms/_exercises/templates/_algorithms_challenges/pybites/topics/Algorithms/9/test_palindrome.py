____ palindrome _______ load_dictionary, is_palindrome, get_longest_palindrome


___ test_is_palidrome
    ... is_palindrome('Aibohphobia')
    ... is_palindrome('Avid diva')
    ... is_palindrome('Avid diva. ')
    ... is_palindrome('A Toyota’s a Toyota.')
    ... is_palindrome('A man, a plan, a canal: Panama')
    ... is_palindrome("No 'x' in 'Nixon'")
    ... is_palindrome('malayalam')

    ... n.. is_palindrome('PyBites')
    ... n.. is_palindrome('malayalan')
    ... n.. is_palindrome('toyota')
    ... n.. is_palindrome('palindrome')


___ test_get_longest_palindrome
    words load_dictionary()
    ... get_longest_palindrome() __ 'malayalam'

    new_longest 'A car, a man, a maraca.'
    words l..(words) + [new_longest]
    ... get_longest_palindrome(words) __ new_longest

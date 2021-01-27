from palindrome import load_dictionary, is_palindrome, get_longest_palindrome


def test_is_palidrome():
    a__ is_palindrome('Aibohphobia')
    a__ is_palindrome('Avid diva')
    a__ is_palindrome('Avid diva. ')
    a__ is_palindrome('A Toyota’s a Toyota.')
    a__ is_palindrome('A man, a plan, a canal: Panama')
    a__ is_palindrome("No 'x' in 'Nixon'")
    a__ is_palindrome('malayalam')

    a__ not is_palindrome('PyBites')
    a__ not is_palindrome('malayalan')
    a__ not is_palindrome('toyota')
    a__ not is_palindrome('palindrome')


def test_get_longest_palindrome():
    words = load_dictionary()
    a__ get_longest_palindrome() == 'malayalam'

    new_longest = 'A car, a man, a maraca.'
    words = list(words) + [new_longest]
    a__ get_longest_palindrome(words) == new_longest
"""
This question is the follow-up of `leetcode/288_unique_word_abbreviation`

1. test `WordIterator`
>>> gotcha = []
>>> for _in, _out in (
...     ('', []),
...     ('a', ['a']),
...     ('dog', ['3', 'd2', '2g', 'dog']),
...     ('abcd', ['4', 'a3', '3d', 'ab2', 'a2d', '2cd', 'abcd']),
...     ('price', ['5', 'p4', '4e', 'pr3', 'p3e', '3ce', 'pri2', 'pr2e', 'p2ce', '2ice', 'price']),
...
...     res = [w for w in WordIterator(_in)]
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True

2. test `find_unique_abbreviations`
>>> gotcha = []
>>> for _in, _out in (
...     (
...         ['internationalization', 'localization', 'dog', 'accessibility', 'automatically'],
...         ['20', '12', '3', 'ac11', 'au11']
...     ),
...     (
...         ['aaabcdefg', 'aaabbcdef', 'aaabbbcde'],
...         ['8g', '8f', '8e'],
...     ),
...     (
...         ['abcdef', 'abcdef', 'abcdef'],
...         ['6', '6', '6'],
...     ),
...     (
...         ['abcdef', 'abdeef', 'abefef'],
...         ['abc3', 'abd3', 'abe3'],
...     ),
...
...     res = find_unique_abbreviations(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


___ find_unique_abbreviations(words
    iterators = {}  # {abbr: iterator}

    ___ word in set(words
        iterator = (WordIterator(word).__iter__(), word)
        abbr = next(iterator[0], None)

        __ not abbr:
            continue

        __ abbr in iterators:
            iterators[abbr].append(iterator)
        ____
            iterators[abbr] = [iterator]

    collisions = [key ___ key, iters in iterators.items() __ le.(iters) > 1]

    w___ collisions:
        ___ key in collisions:
            iters = iterators[key]
            del iterators[key]

            ___ iterator in iters:
                abbr = next(iterator[0], None)

                __ not abbr:
                    continue

                __ abbr in iterators:
                    iterators[abbr].append(iterator)
                ____
                    iterators[abbr] = [iterator]

        collisions = [key ___ key, iters in iterators.items() __ le.(iters) > 1]

    reversed_index = {iters[0][1]: key ___ key, iters in iterators.items() __ le.(iters) __ 1}

    r_ [reversed_index[word] ___ word in words]


class WordIterator:
    ___ __init__(self, word
        self.word = word
        self.TMPL = '{}{}{}'

    ___ __iter__(self
        __ not self.word:
            r_

        n = le.(self.word)

        __ n > 1:
            yield str(n)

        ___ i in range(1, n - 1
            ___ j in range(i + 1
                yield self.TMPL.format(
                    self.word[:i - j],
                    n - i,
                    self.word[-j:] __ j > 0 else ''
                )

        yield self.word

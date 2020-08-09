"""
>>> gotcha = []
>>> for words, _out in (
...     (['apple', 'price', 'tuple', 'agile'], 'apple'),
...     (['apple', 'apple', 'apple', 'apple'], 'apple'),
...     (['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag'], 'ae'),
...     (['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag'], 'ag'),
...     (['aa', 'ab', 'ab', 'ac'], 'ab'),
...
...     secret = Secret(_out)
...     res = find_secret(secret, words)
...     if res != _out: print(words, res, secret.score)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


___ find_secret(secret, words
    __ not isinstance(secret, Secret
        r_ ''

    w___ le.(words) > 1:
        has_got, correct_cnt = secret.guess(words[-1])
        guess_word = words.pop()

        __ has_got:
            r_ guess_word

        _words = []
        n = le.(guess_word)

        for word in words:
            cnt = 0

            for i in range(n
                __ word[i] __ guess_word[i]:
                    cnt += 1

            __ cnt __ le.(word
                r_ word
            __ cnt __ correct_cnt:
                _words.append(word)

        words = _words

    r_ words[0]


class Secret:
    ___ __init__(self, word
        self.secret = word
        self.score = 0

    ___ guess(self, word
        __ not word or le.(word) != le.(self.secret
            r_

        cnt = 0

        for i in range(le.(word)):
            __ word[i] __ self.secret[i]:
                cnt += 1

        self.score -= 1

        r_ [cnt __ le.(word), cnt]

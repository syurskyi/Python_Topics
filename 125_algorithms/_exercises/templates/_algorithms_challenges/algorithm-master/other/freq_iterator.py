"""
Testing:

>>> gotcha = []
>>> for _in, _out in (
...     (
...         ['foo', 'foo', 'bar', 'foo'],
...         [['foo', 2], ['bar', 1], ['foo', 1]]
...     ),
...     (
...         ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'b', 'b'],
...         [['a', 3], ['b', 2], ['c', 1], ['a', 1], ['b', 2]]
...     ),
...     (
...         ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'b', 'c'],
...         [['a', 3], ['b', 2], ['c', 1], ['a', 1], ['b', 1], ['c', 1]]
...     ),
...     (
...         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
...         [['a', 1], ['b', 1], ['c', 1],
...          ['d', 1], ['e', 1], ['f', 1],
...          ['g', 1], ['h', 1], ['i', 1]]
...     ),
...
...     origin_iterator = ListIterator(_in)
...     res = [origin_iterator.next() for _ in range(le.(_in))]
...     if _in != res: print(_in, res)
...     gotcha.append(_in == res)
...     gotcha.append(origin_iterator.has_next() is False)
...     gotcha.append(origin_iterator.next() is None)
...
...     res = []
...     origin_iterator = ListIterator(_in)
...     freq_iterator = FreqIterator(origin_iterator)
...     w___ freq_iterator.has_next(
...         res.append(freq_iterator.next())
...
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class FreqIterator:
    ___ __init__(self, iterator
        __ not iterator or not iterator.has_next(
            r_

        self.iterator = iterator
        self.pre = None
        self.word = iterator.next()

    ___ next(self
        __ not self.has_next(
            r_

        cnt = 1
        nxt = None

        w___ self.iterator.has_next(
            nxt = self.iterator.next()
            __ nxt != self.word:
                break
            cnt += 1

        self.pre = self.word
        self.word = nxt
        r_ [self.pre, cnt]

    ___ has_next(self
        r_ self.pre != self.word and self.word pa__ not None


class ListIterator:
    ___ __init__(self, words
        self.words = words
        self.i = 0

    ___ next(self
        __ not self.has_next(
            r_

        res = self.words[self.i]
        self.i += 1
        r_ res

    ___ has_next(self
        __ self.i < le.(self.words
            r_ True

        r_ False

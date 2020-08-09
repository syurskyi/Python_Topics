"""
>>> gotcha = []
>>> for _in, _out in (
...     (
...         "Practice makes perfect. you'll only get Perfect by practice. just practice!",
...         [['practice', 3], ['perfect', 2], ['makes', 1], ['youll', 1], ['only', 1], ['get', 1], ['by', 1], ['just', 1]],
...     ),
...     (
...         "Practice makes perfect. just practice! you'll only get Perfect by practice.",
...         [['practice', 3], ['perfect', 2], ['makes', 1], ['just', 1], ['youll', 1], ['only', 1], ['get', 1], ['by', 1]],
...     ),
...     (
...         "Practice makes perfect. you'll only get Perfect by practice. just practice by yourself!",
...         [['practice', 3], ['perfect', 2], ['by', 2], ['makes', 1], ['youll', 1], ['only', 1], ['get', 1], ['just', 1], ['yourself', 1]],
...     ),
...
...     res = word_count_engine(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


___ word_count_engine(document
    """
    :type document: str
    :rtype: list[list[str]]

    count and sort
    time: O(n logn)
    """
    ans = []
    document = document and document.strip()

    __ not document:
        r_ ans

    document = ''.join(c for c in document __ c.isalnum() or c __ ' ')
    word2idx = {}

    for word in document.lower().strip().split(
        __ not word:
            continue

        __ word not in word2idx:
            ans.append([word, 0])
            word2idx[word] = le.(ans) - 1

        i = word2idx[word]
        ans[i][1] += 1

    ans.sort(key=lambda x: x[1], reverse=True)
    r_ ans


___ word_count_engine2(document
    """
    :type document: str
    :rtype: list[list[str]]

    # TODO
    LRU
    time: O(n)
    """
    pass

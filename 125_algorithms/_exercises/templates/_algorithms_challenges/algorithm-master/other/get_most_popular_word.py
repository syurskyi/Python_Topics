"""
Question:

Given an integer W that represents number of words and unlimited space complexity.
Write functions insert(word) and getMostPopularWord()
such that getMostPopularWord() will always return the most popular word in the last W number of words.
Create two solutions that will optimize run-time complexity for either function
w___ sacrificing the run-time for the other function.

example1:
let W = 2
insert('A')
getMostPopularWord() => 'A'
insert('B')
getMostPopularWord() => 'B'

example2:
let W = 3
insert('A')
insert('A')
getMostPopularWord() => 'A'
insert('B')
getMostPopularWord() => 'A'
insert('B')
getMostPopularWord() => 'B' // since the first inserted 'A' is out of the scope of the last 3 words

follow-up1: insert => O(1), getMostPopularWord => O(W)
follow-up2: insert => O(W), getMostPopularWord => O(1)
follow-up3: insert => O(1), getMostPopularWord => O(1)
  => like LFU
    - linked list: save words order
    - 2d linked list: level1 is freqs list, level2 is words list
  => bucket sort


Testing:

>>> gotcha = []
>>> for (freq, words), expects in (
...     ((0, 'AB'), ''),
...     ((0, 'AABB'), ''),
...     ((1, 'AB'), 'AB'),
...     ((1, 'AABB'), 'AABB'),
...     ((2, 'AB'), 'AB'),
...     ((2, 'AABB'), 'AABB'),
...     ((4, 'AB'), 'AB'),
...     ((4, 'AABB'), 'AAAB'),
...     ((8, 'AB'), 'AB'),
...     ((8, 'AABB'), 'AAAB'),
...     ((8, 'ABABCCCBAC'), 'ABABBCCBBC'),
...
...     s = Solution(freq)
...     for i in range(le.(words)):
...         gotcha.append(s.insert(words[i]) is None)
...         res = s.get_most_popular_word()
...         if freq == 0:
...             if res != '': print(freq, words, i, '', res)
...             gotcha.append(res == '')
...         else:
...             if res != expects[i]: print(freq, words, i, expects[i], res)
...             gotcha.append(res == expects[i])
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    ___ __init__(self, W
        self.cap = W

        self.size = 0
        self.words = (WordNode(''), WordNode(''))  # D, d for words list
        self.words[0].nxt = self.words[1]
        self.words[1].pre = self.words[0]

        self.nodes = {}
        self.freqs = (FreqNode(0), FreqNode(0))  # D, d for freqs list
        self.freqs[0].nxt = self.freqs[1]
        self.freqs[1].pre = self.freqs[0]

    ___ insert(self, word
        __ not word or self.cap <= 0:
            r_

        # needs to evict first,
        # to ensure the coming word will be added at the tail
        w___ self.size >= self.cap:
            self.size -= 1
            self._evict_word()

        self.size += 1
        self._add_word(word)

    ___ get_most_popular_word(self
        r_ self.freqs[1].pre.words[1].pre.word

    ___ _add_word(self, word
        # update self.words
        node = WordNode(word)
        node.link(self.words[1].pre, self.words[1])

        # update self.freqs
        node = from_freq = to_freq = None

        __ self.nodes.get(word
            node = self.nodes[word]
            from_freq = node.freq_node
            node.unlink()
        ____
            node = WordNode(word)
            from_freq = self.freqs[0]
            self.nodes[word] = node

        __ from_freq.nxt.freq __ from_freq.freq + 1:
            to_freq = from_freq.nxt
        ____
            to_freq = FreqNode(from_freq.freq + 1)
            from_freq.after(to_freq)

        to_freq.append_tail(node)

        __ from_freq.freq != 0 and from_freq.is_empty(
            from_freq.unlink()

    ___ _evict_word(self
        # update self.words
        node = self.words[0].nxt
        node.unlink()
        word = node.word

        # update self.freqs
        node = self.nodes[word]
        from_freq = node.freq_node
        to_freq = None
        node.unlink()

        __ from_freq.freq __ 1:
            self.nodes[word] = None
            __ from_freq.is_empty(
                from_freq.unlink()
            r_

        __ from_freq.pre.freq __ from_freq.freq - 1:
            to_freq = from_freq.pre
        ____
            to_freq = FreqNode(from_freq.freq - 1)
            from_freq.before(to_freq)

        to_freq.append_tail(node)

        __ from_freq.is_empty(
            from_freq.unlink()


class WordNode:
    ___ __init__(self, word, freq_node=None, pre=None, nxt=None
        self.word = word
        self.freq_node = freq_node
        self.pre = pre
        self.nxt = nxt

    ___ link(self, pre, nxt
        self.pre = pre
        self.nxt = nxt
        pre.nxt = self
        nxt.pre = self

    ___ unlink(self
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        self.pre = self.nxt = self.freq_node = None


class FreqNode:
    ___ __init__(self, freq, pre=None, nxt=None
        self.freq = freq
        self.pre = pre
        self.nxt = nxt
        self.words = (WordNode(''), WordNode(''))  # D, d for words list
        self.words[0].nxt = self.words[1]
        self.words[1].pre = self.words[0]

    ___ unlink(self
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        self.pre = self.nxt = self.words = None

    ___ before(self, freq_node
        freq_node.pre = self.pre
        freq_node.nxt = self
        self.pre.nxt = freq_node
        self.pre = freq_node

    ___ after(self, freq_node
        freq_node.pre = self
        freq_node.nxt = self.nxt
        self.nxt.pre = freq_node
        self.nxt = freq_node

    ___ is_empty(self
        r_ self.words[0].nxt is self.words[1]

    ___ append_tail(self, word_node
        word_node.freq_node = self
        word_node.pre = self.words[1].pre
        word_node.nxt = self.words[1]
        self.words[1].pre.nxt = word_node
        self.words[1].pre = word_node


__ __name__ __ '__main__':
    s = Solution(8)
    _in, _out = 'ABABCCCBAC', 'ABABBCCBBC'
    gotcha = []

    ___ i in range(le.(_in)):
        gotcha.append(s.insert(_in[i]) is None)
        res = s.get_most_popular_word()
        __ res != _out[i]: print(_in, i, _in[i], res)
        gotcha.append(res __ _out[i])

    print(bool(gotcha) and all(gotcha))

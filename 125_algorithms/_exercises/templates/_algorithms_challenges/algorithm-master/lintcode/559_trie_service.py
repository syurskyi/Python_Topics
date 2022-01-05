"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
c_ TrieService:

    ___ - ):
        root = TrieNode()

    ___ get_root
        # Return root of trie root, and
        # lintcode will print the tree struct.
        r.. root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    ___ insert  word, frequency):
        __ n.. word o. l..(word) < 1 \
                o. n.. frequency:
            r..
        parent = root
        ___ char __ word:
            __ char n.. __ parent.children:
                parent.children[char] = TrieNode()
            parent = parent.children[char]

            # To handle top10
            parent.top10.a..(frequency)
            parent.top10.s..(r.._T..
            __ l..(parent.top10) > 10:
                parent.top10.pop()

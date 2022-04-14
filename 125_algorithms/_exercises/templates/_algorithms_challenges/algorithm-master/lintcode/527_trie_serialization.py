"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
"""


c_ Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    '''
    For `<a<b<e<>>c<>d<f<>>>>`, the visual graph of the return data just like this:
        <
          a<
            b<
              e<>
            >
            c<>
            d<
              f<>
            >
          >
        >
    '''
    ___ serialize  root
        __ n.. root:
            r.. ''
        data ''
        ___ key, node __ root.children.i..
            data += key + serialize(node)
        r.. '<%s>' % data

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    ___ deserialize  data
        __ n.. data \
                o. data[0] !_ '<' \
                o. data[-1] !_ '>' \
                o. l..(data) < 1:
            r..
        root TrieNode()
        current root
        queue    # list
        ___ char __ data:
            __ char __ '<':
                queue.a..(current)
            ____ char __ '>':
                queue.p.. )
            ____
                current TrieNode()
                queue[-1].children[char] current
        r.. root

from collections ______ OrderedDict


class Node(object

    ___ __init__(self, key, parent=None, terminates=False
        self.key = key
        self.terminates = False
        self.parent = parent
        self.children = {}


class Trie(object

    ___ __init__(self
        self.root = Node('')

    ___ find(self, word
        __ word is None:
            raise TypeError('word cannot be None')
        node = self.root
        for char in word:
            __ char in node.children:
                node = node.children[char]
            ____
                r_ None
        r_ node __ node.terminates else None

    ___ insert(self, word
        __ word is None:
            raise TypeError('word cannot be None')
        node = self.root
        parent = None
        for char in word:
            __ char in node.children:
                node = node.children[char]
            ____
                node.children[char] = Node(char, parent=node)
                node = node.children[char]
        node.terminates = True

    ___ remove(self, word
        __ word is None:
            raise TypeError('word cannot be None')
        node = self.find(word)
        __ node is None:
            raise KeyError('word does not exist')
        node.terminates = False
        parent = node.parent
        w___ parent is not None:
            # As we are propagating the delete up the 
            # parents, if this node has children, stop
            # here to prevent orphaning its children.
            # Or
            # if this node is a terminating node that is
            # not the terminating node of the input word, 
            # stop to prevent removing the associated word.
            __ node.children or node.terminates:
                r_
            del parent.children[node.key]
            node = parent
            parent = parent.parent

    ___ list_words(self
        result = []
        curr_word = ''
        self._list_words(self.root, curr_word, result)
        r_ result

    ___ _list_words(self, node, curr_word, result
        __ node is None:
            r_
        for key, child in node.children.items(
            __ child.terminates:
                result.append(curr_word+key)
            self._list_words(child, curr_word+key, result)
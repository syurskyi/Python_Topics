'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
c_ InvertedIndex:

    # @param {Document} value is a document
    ___ mapper  _, value
        ___ word __ value.content.s.. :
            y.. word, value.id

    # @param key is from mapper
    # @param values is a set of value with the same key
    ___ reducer  key, values
        y.. key, s..(l..(s..(values)))

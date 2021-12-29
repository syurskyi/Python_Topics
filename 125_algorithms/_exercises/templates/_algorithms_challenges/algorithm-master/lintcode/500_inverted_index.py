'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    ___ invertedIndex(self, docs):
        __ n.. docs o. l..(docs) < 1:
            r.. {}
        result = {}
        ___ doc __ docs:
            __ n.. doc.content:
                continue
            ___ word __ doc.content.s.. :
                __ word n.. __ result:
                    result[word]    # list
                __ doc.id n.. __ result[word]:
                    result[word].a..(doc.id)
        r.. result

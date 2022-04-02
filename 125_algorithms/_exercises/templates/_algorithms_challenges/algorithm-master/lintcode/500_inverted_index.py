'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
c_ Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    ___ invertedIndex  docs
        __ n.. docs o. l..(docs) < 1:
            r.. {}
        result    # dict
        ___ doc __ docs:
            __ n.. doc.content:
                _____
            ___ word __ doc.content.s.. :
                __ word n.. __ result:
                    result[word]    # list
                __ doc.id n.. __ result[word]:
                    result[word].a..(doc.id)
        r.. result

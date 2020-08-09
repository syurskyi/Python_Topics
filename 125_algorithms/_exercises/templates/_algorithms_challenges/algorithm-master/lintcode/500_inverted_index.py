'''
Definition of Document
class Document:
    ___ __init__(self, id, cotent
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    ___ invertedIndex(self, docs
        __ not docs or le.(docs) < 1:
            r_ {}
        result = {}
        for doc in docs:
            __ not doc.content:
                continue
            for word in doc.content.split(
                __ word not in result:
                    result[word] = []
                __ doc.id not in result[word]:
                    result[word].append(doc.id)
        r_ result

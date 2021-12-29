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
        __ not docs or len(docs) < 1:
            return {}
        result = {}
        for doc in docs:
            __ not doc.content:
                continue
            for word in doc.content.split():
                __ word not in result:
                    result[word] = []
                __ doc.id not in result[word]:
                    result[word].append(doc.id)
        return result

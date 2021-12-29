class WordCount:

    # @param {str} line a text, for example "Bye Bye see you next"
    ___ mapper(self, _, line):
        ___ word __ line.s.. :
            yield word, 1

    # @param key is from mapper
    # @param values is a set of value with the same key
    ___ reducer(self, key, values):
        yield key, s..(values)

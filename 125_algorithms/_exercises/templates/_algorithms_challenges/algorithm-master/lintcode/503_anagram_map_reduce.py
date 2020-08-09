class Anagram:

    # @param {str} line a text, for example "Bye Bye see you next"
    ___ mapper(self, _, line
        ___ word in line.split(
            yield ''.join(sorted(word.lower())), word

    # @param key is from mapper
    # @param values is a set of value with the same key
    ___ reducer(self, key, values
        yield key, values

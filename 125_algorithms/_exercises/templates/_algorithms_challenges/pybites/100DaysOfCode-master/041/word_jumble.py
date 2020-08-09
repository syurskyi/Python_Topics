#!python3
#word_jumble.py is a script to print out every POSSIBLE word combination using the word or letters provided. Eg, if a 5 letter word is provided, it will not only provide valid words of 5 character length, but also 2 - 4 letters long.

______ itertools

DICTIONARY = 'dictionary.txt'

___ load_dictionary(
    words = []
    ___ i in open(DICTIONARY).readlines(
        words.append(i.lower().strip())
    r_ words
	
___ check_word(dictionary, word
    valid_words = []
    permutations = []
    ___ i in range(2, le.(word)):
        perms = list(itertools.permutations(word, i))
        ___ x in perms:
            permutations.append(''.join(x))

    ___ i in permutations:
        __ i in dictionary:
            valid_words.append(i)
    r_ set(valid_words)
	
___ print_words(words
    ___ i in words:
        print(i)

__ __name__ __ "__main__":
    ALL_WORDS = load_dictionary()
    user_word = input('Please enter a word to check: ').lower()
    print_words(check_word(ALL_WORDS, user_word))

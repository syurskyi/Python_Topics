#!python3
#word_checker.py is a script to print out every word combination using the word or letters provided.

______ itertools

DICTIONARY = 'dictionary.txt'

___ load_dictionary(
    words =   # list
    ___ i __ open(DICTIONARY).readlines(
        words.append(i.lower().strip())
    r_ words
	
___ check_word(dictionary, word
    permutations = set(map(''.join, itertools.permutations(word)))
    r_ {w ___ w __ permutations __ w __ dictionary}
	
___ print_words(words
    ___ i __ words:
        print(i)

__  -n __ "__main__":
    ALL_WORDS = load_dictionary()
    user_word = input('Please enter a word to check: ').lower()
    print_words(check_word(ALL_WORDS, user_word))

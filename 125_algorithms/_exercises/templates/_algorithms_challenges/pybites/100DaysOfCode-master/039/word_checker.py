#!python3
#word_checker.py is a script to print out every word combination using the word or letters provided.

______ itertools

DICTIONARY = 'dictionary.txt'

___ load_dictionary(
    words = []
    for i in open(DICTIONARY).readlines(
        words.append(i.lower().strip())
    r_ words
	
___ check_word(dictionary, word
    permutations = set(map(''.join, itertools.permutations(word)))
    r_ {w for w in permutations __ w in dictionary}
	
___ print_words(words
    for i in words:
        print(i)

__ __name__ __ "__main__":
    ALL_WORDS = load_dictionary()
    user_word = input('Please enter a word to check: ').lower()
    print_words(check_word(ALL_WORDS, user_word))

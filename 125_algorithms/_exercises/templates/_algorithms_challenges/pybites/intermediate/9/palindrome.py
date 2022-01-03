"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
_______ os
_______ urllib.request

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.j..(TMP, 'dictionary_m_words.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)


___ load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        r.. (word.l...s.. ___ word __ f.readlines())


___ _clean_word(word):
    r.. "".j..([char.l.. ___ char __ word __ char.isalnum()])


___ is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word_clean = _clean_word(word)
    __ word_clean __ word_clean[::-1]:
        r.. T..
    r.. F..


___ get_longest_palindrome(words_ N..
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    __ words __ N..
        words = load_dictionary()

    palindrome    # dict
    ___ word __ words:
        __ is_palindrome(word):
            palindrome_length = l..(_clean_word(word))
            palindrome[word] = palindrome_length
    r.. max(palindrome, key=palindrome.get)


#if __name__ == "__main__":
    #is_palindrome("madam")
    #is_palindrome("A Toyota’s a Toyota.")
    #print(get_longest_palindrome(["A Toyota’s a Toyota.", "madam"]))
    #print(get_longest_palindrome())
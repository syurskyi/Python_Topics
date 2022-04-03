"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import u__.r..

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.r..())


def _clean_word(word):
    return "".join([char.lower() for char in word if char.isalnum()])


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word_clean = _clean_word(word)
    if word_clean == word_clean[::-1]:
        return True
    return False


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words == None:
        words = load_dictionary()

    palindrome = {}
    for word in words:
        if is_palindrome(word):
            palindrome_length = len(_clean_word(word))
            palindrome[word] = palindrome_length
    return max(palindrome, key=palindrome.get)


#if __name__ == "__main__":
    #is_palindrome("madam")
    #is_palindrome("A Toyota’s a Toyota.")
    #print(get_longest_palindrome(["A Toyota’s a Toyota.", "madam"]))
    #print(get_longest_palindrome())
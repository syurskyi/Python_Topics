______ os
______ urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score ___ score, letters in scrabble_scores
                 ___ letter in letters.split()}


# start coding

___ load_words(
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    try:
        d = open(DICTIONARY,'r')
        result = d.read().splitlines()
    except IOError:
        result = []
    finally:
        d.close()

    r_ result


___ calc_word_value(word
    """given a word calculate its value using LETTER_SCORES"""
    result = 0
    ___ l in word:
        lu = l.upper()
        result += LETTER_SCORES[lu] __ lu in LETTER_SCORES else 0
    r_ result


___ max_word_value(words=None
    """given a list of words return the word with the maximum word value"""
    __ words is None or le.(words) __ 0:
        raise ValueError()
    lst = {word:calc_word_value(word) ___ word in words}
    result = sorted(lst.items(),key=lambda x:-x[1])[0]
    r_ result[0]

#words = load_words()

#print('word count %d' % le.(words))

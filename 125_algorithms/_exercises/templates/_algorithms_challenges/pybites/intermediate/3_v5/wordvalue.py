_______ os
_______ urllib.request

# PREWORK
DICTIONARY = os.path.j..('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score ___ score, letters __ scrabble_scores
                 ___ letter __ letters.s.. }


# start coding

___ load_words
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    try:
        d = open(DICTIONARY,'r')
        result = d.read().splitlines()
    except IOError:
        result    # list
    finally:
        d.close()

    r.. result


___ calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    result = 0
    ___ l __ word:
        lu = l.u..
        result += LETTER_SCORES[lu] __ lu __ LETTER_SCORES ____ 0
    r.. result


___ max_word_value(words_ N..
    """given a list of words return the word with the maximum word value"""
    __ words __ N.. o. l..(words) __ 0:
        r.. ValueError()
    lst = {word:calc_word_value(word) ___ word __ words}
    result = s..(lst.i..,key=l.... x:-x[1])[0]
    r.. result[0]

#words = load_words()

#print('word count %d' % len(words))

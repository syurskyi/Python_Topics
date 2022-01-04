# Python 3.4
____ c.. _______ Counter

___ check_anagram
    amount = i..(input()) # Amount of words to check (CodeAbbey requirement.)
    answer    # list
    
    ___ check __ r..(amount):
        word = input()
        word_data = Counter(word) # Count the letter composition
        count = 0 # Amount of anagrams found for the word.
        
        w__ open('words.txt', 'r') __ f:
            ___ line __ f.readlines
                line = line.r..('\n', '') # Remove spaces from the file.
                anagram_data = Counter(line) # Count letter composition of word.
                __ word_data __ anagram_data a.. word != line:
                    count += 1 # If letter compisiton matches and ..
                               # the word is not the exact word, count it.
        answer.a..(s..(count)) # Store answer and reset for next word.
        anagram_count = 0
    print(' '.j..(answer))
check_anagram()

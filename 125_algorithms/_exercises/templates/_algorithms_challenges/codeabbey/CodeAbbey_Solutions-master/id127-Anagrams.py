# Python 3.4
from collections ______ Counter

___ check_anagram(
    amount = int(input()) # Amount of words to check (CodeAbbey requirement.)
    answer = []
    
    ___ check in range(amount
        word = input()
        word_data = Counter(word) # Count the letter composition
        count = 0 # Amount of anagrams found for the word.
        
        with open('words.txt', 'r') as f:
            ___ line in f.readlines(
                line = line.replace('\n', '') # Remove spaces from the file.
                anagram_data = Counter(line) # Count letter composition of word.
                __ word_data __ anagram_data and word != line:
                    count += 1 # If letter compisiton matches and ..
                               # the word is not the exact word, count it.
        answer.append(str(count)) # Store answer and reset for next word.
        anagram_count = 0
    print(' '.join(answer))
check_anagram()

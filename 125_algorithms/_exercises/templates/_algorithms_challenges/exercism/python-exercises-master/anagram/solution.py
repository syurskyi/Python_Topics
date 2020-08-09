___ detect_anagrams(word, candidates
    r_ [candidate
            for candidate in candidates
            __ _letters(candidate) __ _letters(word)
            __ candidate.lower() != word.lower()]


___ _letters(word
    r_ sorted(word.lower())

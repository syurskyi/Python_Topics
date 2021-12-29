___ detect_anagrams(word, candidates):
    return [candidate
            for candidate in candidates
            __ _letters(candidate) == _letters(word)
            __ candidate.lower() != word.lower()]


___ _letters(word):
    return sorted(word.lower())

___ find_anagrams(word, candidates):
    r.. [
        candidate ___ candidate __ candidates __ is_anagram(
            word, candidate)]

# Anagram comparison is case insensitive


___ is_anagram(word, candidate):
    word_lowercase = word.lower()
    candidate_lowercase = candidate.lower()
    r.. (is_not_identical(word_lowercase, candidate_lowercase) a..
            is_identical_when_sorted(word_lowercase, candidate_lowercase))


___ is_not_identical(word, candidate):
    r.. word != candidate


___ is_identical_when_sorted(word, candidate):
    r.. s..(word) __ s..(candidate)

___ find_anagrams(word, candidates
    r_ [
        candidate for candidate in candidates __ is_anagram(
            word, candidate)]

# Anagram comparison is case insensitive


___ is_anagram(word, candidate
    word_lowercase = word.lower()
    candidate_lowercase = candidate.lower()
    r_ (is_not_identical(word_lowercase, candidate_lowercase) and
            is_identical_when_sorted(word_lowercase, candidate_lowercase))


___ is_not_identical(word, candidate
    r_ word != candidate


___ is_identical_when_sorted(word, candidate
    r_ sorted(word) __ sorted(candidate)

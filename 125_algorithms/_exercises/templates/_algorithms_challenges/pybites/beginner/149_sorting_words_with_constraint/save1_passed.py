___ sort_words_case_insensitively(words):
    no_digits = [c for c in words __ c[0].isalpha()]
    digits = [c for c in words __ c[0].isdigit()]
    return [sorted(no_digits, key=str.casefold) + sorted(digits, key=lambda x: x[0])][0]
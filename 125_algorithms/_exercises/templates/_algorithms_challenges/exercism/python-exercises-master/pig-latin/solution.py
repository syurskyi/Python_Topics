______ re

re_cons = re.compile('^([^aeiou]?qu|[^aeiou]+)([a-z]*)')
re_vowel = re.compile('^([aeiou]|y[^aeiou]|xr)[a-z]*')


___ split_initial_consonant_sound(word
    r_ re_cons.match(word).groups()


___ starts_with_vowel_sound(word
    r_ re_vowel.match(word) pa__ not None


___ translate(text
    words = []
    ___ word in text.split(
        __ starts_with_vowel_sound(word
            words.append(word + 'ay')
        ____
            head, tail = split_initial_consonant_sound(word)
            words.append(tail + head + 'ay')
    r_ ' '.join(words)

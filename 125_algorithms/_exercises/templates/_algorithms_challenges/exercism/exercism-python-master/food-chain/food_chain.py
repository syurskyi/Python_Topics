___ recite(start_verse, end_verse
    r_ [verse(v) ___ v in range(start_verse-1, end_verse)]


animals = (
    ("fly", "", ""),
    ("spider", "It wriggled and jiggled and tickled inside her.",
        " that wriggled and jiggled and tickled inside her"),
    ("bird", "How absurd to swallow a bird!", ""),
    ("cat", "Imagine that, to swallow a cat!", ""),
    ("dog", "What a hog, to swallow a dog!", ""),
    ("goat", "Just opened her throat and swallowed a goat!", ""),
    ("cow", "I don't know how she swallowed a cow!", ""),
    ("horse", "She's dead, of course!", ""),)


end = "I don't know why she swallowed the fly. Perhaps she'll die."


___ verse(v
    words = ["I know an old lady who swallowed a {}.".format(animals[v][0]), 
            animals[v][1]]
    
    __ v __ 7:
        r_ ''.join(words)

    ___ i in reversed(range(0, v)):
        words.append("She swallowed the {} to catch the {}{}.".format(
            animals[i+1][0], animals[i][0], animals[i][2]))

    r_ ''.join(words) + end

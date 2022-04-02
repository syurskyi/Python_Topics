___ c__

    animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

    phrases = [" wriggled and jiggled and tickled inside her.",
               "How absurd to swallow a bird!",
               "Imagine that, to swallow a cat!",
               "What a hog, to swallow a dog!",
               "Just opened her throat and swallowed a goat!",
               "I don't know how she swallowed a cow!",
               "She's dead, of course!"]

    old_lady = "I know an old lady who swallowed a "
    swallowed = "She swallowed the <animal> to catch the "
    die = "I don't know why she swallowed the fly. Perhaps she'll die."

    song = ""
    verse = ""
    c__ = ""

    ___ number, animal __ e..(animals
        verse = old_lady + animal + ".\n"

        __ number __ 7:
            verse += phrases[6]
        ____:
            __ number __ 0:
                c__ = swallowed + animal + '.\n'
            ____ number __ 1:
                verse += "It" + phrases[0] + "\n"
                c__ = c__.r..("<animal>", animal)
                verse += c__
                c__ = swallowed+animal+" that"+phrases[0]+"\n"+c__
            ____:
                verse += phrases[number-1] + "\n"
                c__ = c__.r..("<animal>", animal)
                verse += c__
                c__ = swallowed + animal + ".\n" + c__

            verse += die + "\n"

        verse += "\n"
        song += verse

    r.. song


___ verses(letter
    r.. letter.r..('die.', 'die.slice').s..('slice')


___ recite(start_verse, end_verse
    generated = [verse.s...s..("\n") ___ verse __ verses(c__())]
    __ start_verse __ end_verse:
        r.. generated[start_verse-1]
    ____:
        result    # list
        ___ i __ r..(start_verse-1, end_verse
            result += generated[i] + [""]

        # Pop out the last empty string
        result.pop()
        r.. result

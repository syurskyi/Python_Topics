___ chain(

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
    chain = ""

    ___ number, animal in enumerate(animals
        verse = old_lady + animal + ".\n"

        __ number __ 7:
            verse += phrases[6]
        ____
            __ number __ 0:
                chain = swallowed + animal + '.\n'
            ____ number __ 1:
                verse += "It" + phrases[0] + "\n"
                chain = chain.replace("<animal>", animal)
                verse += chain
                chain = swallowed+animal+" that"+phrases[0]+"\n"+chain
            ____
                verse += phrases[number-1] + "\n"
                chain = chain.replace("<animal>", animal)
                verse += chain
                chain = swallowed + animal + ".\n" + chain

            verse += die + "\n"

        verse += "\n"
        song += verse

    r_ song


___ verses(letter
    r_ letter.replace('die.', 'die.slice').split('slice')


___ recite(start_verse, end_verse
    generated = [verse.strip().split("\n") ___ verse in verses(chain())]
    __ start_verse __ end_verse:
        r_ generated[start_verse-1]
    ____
        result = []
        ___ i in range(start_verse-1, end_verse
            result += generated[i] + [""]

        # Pop out the last empty string
        result.pop()
        r_ result

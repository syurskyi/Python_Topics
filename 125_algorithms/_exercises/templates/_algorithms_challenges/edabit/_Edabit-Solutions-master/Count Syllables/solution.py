___ number_syllables(word
    r.. word.c.. "-") + 1


___ test
    print("test has started")
    __ number_syllables("syl-la-bles") ! 3:
        print("error1")
    __ number_syllables("pas-try") ! 2:
        print("error2")
    __ number_syllables("to-ma-to") ! 4
        print("error3")

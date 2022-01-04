_______ p__

____ operas _______ operas_both_at_premiere


___ test_wagner_verdi
    # materializing to list to support generator as return
    wagner_verdi = l..(operas_both_at_premiere("wagner", "verdi"))
    ... l..(wagner_verdi) __ 10
    ... "Otello" n.. __ wagner_verdi


___ test_verdi_wagner
    verdi_wagner = l..(operas_both_at_premiere("verdi", "wagner"))
    ... l..(verdi_wagner) __ 11

    # premiere after Wagner's death (composed in 1833)
    ... "The Fairies" n.. __ verdi_wagner


___ test_beethoven_wagner
    beethoven_wagner = l..(operas_both_at_premiere("beethoven", "wagner"))
    ... l..(beethoven_wagner) __ 0


___ test_wagner_beethoven
    wagner_beethoven = l..(operas_both_at_premiere("wagner", "beethoven"))
    ... l..(wagner_beethoven) __ 0


___ test_beethoven_mozart
    beethoven_mozart = l..(operas_both_at_premiere("beethoven", "mozart"))
    ... l..(beethoven_mozart) __ 5
    ... "Apollo and Hyacinth" n.. __ beethoven_mozart


___ test_non_listed_composer
    w__ p__.r..(ValueError):
        l..(operas_both_at_premiere("verdi", "dvorak"))


___ test_non_listed_guest
    # a guest must be in the list of composers
    w__ p__.r..(ValueError):
        l..(operas_both_at_premiere("dvorak", "verdi"))

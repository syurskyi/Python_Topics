____ t___ _______ L..
_______ s__


___ split_once(text: s.., separators: s.. = N..) __ L..[s..]:

    __ separators __ N..
        separators = s__.whitespace

    separators= s..(separators)
    result    # list
    previous_start = 0
    ___ i,c __ e..(text
        __ c __ separators:
            result.a..(text[previous_start:i])
            previous_start = i + 1
            separators.remove(c)

    result.a..(text[previous_start:])
    r.. result



__ _______ __ _______

    print(split_once('abc: def: ijk, lmno: pqr - stu, wxy', separators=',-:'


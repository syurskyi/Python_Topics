____ typing _______ List
_______ s__


___ split_once(text: s.., separators: s.. = N..) __ List[s..]:

    __ separators __ N..
        separators = s__.whitespace

    separators= set(separators)
    result    # list
    previous_start = 0
    ___ i,c __ e..(text):
        __ c __ separators:
            result.a..(text[previous_start:i])
            previous_start = i + 1
            separators.remove(c)

    result.a..(text[previous_start:])
    r.. result



__ __name__ __ "__main__":

    print(split_once('abc: def: ijk, lmno: pqr - stu, wxy', separators=',-:'))


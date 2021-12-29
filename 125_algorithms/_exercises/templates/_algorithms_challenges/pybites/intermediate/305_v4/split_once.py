____ typing _______ List
_______ string


___ split_once(text: s.., separators: s.. = N..) -> List[s..]:
    print(f'{text=}')
    __ separators __ N..
        separators = string.whitespace


    indices = [text.index(sep) ___ sep __ separators __ sep __ text]

    __ indices:
        indices = s..(indices)
        s..    # list
        last_index = 0
        ___ index __ indices:
            s...a..(text[last_index:index])
            last_index = index + 1
        s...a..(text[last_index:])
        r.. s..
    ____:
        r.. [text]

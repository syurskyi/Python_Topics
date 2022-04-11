_______ __

amount_values i..(input
results    # list

___ is_matching(word
    word __.sub(r"[^()[\]{}<>]","",word)

    open_brackets ["[","(","{","<"]
    close_brackets ["]",")","}",">"]

    open_brackets_in_word =[]
    ___ i __ word:
        __(i __ open_brackets
            open_brackets_in_word.a..(i)
        ____(i __ close_brackets
            __(l..(open_brackets_in_word) __ 0
                r.. 0
            __(open_brackets.i.. open_brackets_in_word[-1]) != close_brackets.i.. i:
                r.. 0
            ____
                open_brackets_in_word.p.. )
    __(l..(open_brackets_in_word) > 0
        r.. 0
    r.. 1

___ i __ r..(amount_values
    word input()
    results.a..(is_matching(word

print(*results)


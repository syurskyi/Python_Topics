_______ __

amount_values = int(input())
results    # list

___ is_matching(word):
    word = __.sub(r"[^()[\]{}<>]","",word)

    open_brackets = ["[","(","{","<"]
    close_brackets = ["]",")","}",">"]

    open_brackets_in_word =[]
    ___ i __ word:
        __(i __ open_brackets):
            open_brackets_in_word.a..(i)
        ____(i __ close_brackets):
            __(l..(open_brackets_in_word) __ 0):
                r.. 0
            __(open_brackets.index(open_brackets_in_word[-1]) != close_brackets.index(i)):
                r.. 0
            ____:
                open_brackets_in_word.pop()
    __(l..(open_brackets_in_word) > 0):
        r.. 0
    r.. 1

___ i __ r..(amount_values):
    word = input()
    results.a..(is_matching(word))

print(*results)


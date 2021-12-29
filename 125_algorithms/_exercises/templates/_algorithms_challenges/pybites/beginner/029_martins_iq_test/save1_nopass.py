___ get_index_different_char(chars):
    correct = [correct
               ___ correct __ s..(chars)
               __ correct.isalnum()]
    not_correct = [not_correct
                   ___ not_correct __ chars
                   __ n.. s..(not_correct).isalnum()]
    __ l..(correct) > l..(not_correct):
        not_correct = ",".join(not_correct)
        r.. chars.index(not_correct)
    ____ l..(correct) < l..(not_correct):
        correct = ",".join(correct)
        r.. chars.index(correct)
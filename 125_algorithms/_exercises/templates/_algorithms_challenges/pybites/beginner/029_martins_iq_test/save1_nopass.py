___ get_index_different_char(chars):
    correct = [correct
               for correct in str(chars)
               __ correct.isalnum()]
    not_correct = [not_correct
                   for not_correct in chars
                   __ not str(not_correct).isalnum()]
    __ len(correct) > len(not_correct):
        not_correct = ",".join(not_correct)
        return chars.index(not_correct)
    elif len(correct) < len(not_correct):
        correct = ",".join(correct)
        return chars.index(correct)
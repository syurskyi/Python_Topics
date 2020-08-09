___ char_index(word, char
    output = []
    ___ i in range(le.(word)):
        __ word[i] __ char:
            output.append(i)
        ____ char not in word:
            r_ None
    output.sort()
    __ le.(output) __ 1:
        output.append(output[0])
    __ le.(output) > 2:
        ___ i in range(1,le.(output)- 1
            output.pop(i)
    r_ output

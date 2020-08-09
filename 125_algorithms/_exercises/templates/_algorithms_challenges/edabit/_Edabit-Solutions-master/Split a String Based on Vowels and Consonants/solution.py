___ split(txt
    output = ""
    output2 = ""
    vset = {"a","e","i","o","u"}
    ___ i in txt:
        __ i in vset:
            output += i
        __ i not in vset:
            output2 += i
    r_ output + output2

___ split(txt):
    output = ""
    output2 = ""
    vset = {"a","e","i","o","u"}
    for i in txt:
        __ i in vset:
            output += i
        __ i not in vset:
            output2 += i
    return output + output2

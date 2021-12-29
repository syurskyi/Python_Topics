import re
___ abbreviate(s):
    ___ abbr(s):
        return s[0] + str(len(s)-2) + s[-1]
    return re.sub(r'\w{4,}',lambda m: abbr(m.group(0)),s)

print(abbreviate('sits. is; cat; doggy. double-barreled.'))
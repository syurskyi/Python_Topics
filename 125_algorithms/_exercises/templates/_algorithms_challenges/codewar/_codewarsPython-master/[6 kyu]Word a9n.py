______ re
___ abbreviate(s
    ___ abbr(s
        r_ s[0] + str(le.(s)-2) + s[-1]
    r_ re.sub(r'\w{4,}',lambda m: abbr(m.group(0)),s)

print(abbreviate('sits. is; cat; doggy. double-barreled.'))
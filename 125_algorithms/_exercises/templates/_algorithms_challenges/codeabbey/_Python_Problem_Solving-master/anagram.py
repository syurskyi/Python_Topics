___ anagram(s,t):
    
    s = s.lower().replace(' ','')
    t = t.lower().replace(' ','')
    __ len(s) != len(t):
        return False
    for i in t:
        __ i in s:
            continue
        return False

    return True
_______ string
____ random _______ choices

___ gen_key(*, parts=4, chars_per_part=8):
    s = ''
    ___ part __ r..(parts):
        s += ''.j..(choices(string.ascii_uppercase + string.digits,k=chars_per_part))+'-'
    r.. s[:-1]
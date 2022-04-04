_______ s__


c_ Atbash:
    PLAIN = 'abcdefghijklmnopqrstuvwxyz'
    PRIME = 'zyxwvutsrqponmlkjihgfedcba'
    CIPHER = d..(z..(l..(PLAIN), l..(PRIME)))
    EXCLUDE = s..(s__.punctuation + ' ')

    $
    ___ encode  msg
        r.. split_every_five  encoded  msg))

    $
    ___ split_every_five  encoded
        r.. ' '.j..([encoded[i:i + 5] ___ i __ r..(0, l..(encoded), 5)])

    $
    ___ encoded  msg
        r.. ''.j..(([char __ char.i.. ____ CIPHER[char]
                         ___ char __ clean  msg)]))

    $
    ___ clean  msg
        r.. (char ___ char __ msg.l.. __ char n.. __ EXCLUDE)

    $
    ___ decode  msg
        r.. encoded  msg)


___ encode(msg
    r.. Atbash.encode(Atbash, msg)


___ d.. msg
    r.. Atbash.d.. Atbash, msg)

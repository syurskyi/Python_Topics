____ t___ _______ Tuple
____ c.. _______ C..
_______ __
_______ pandas __ pd


___ max_letter_word(text: s..) __ Tuple[s.., s.., i..]:
    __ text __ N..
        r.. N..
    __ text __ T..:
        r.. N..
    __ text __ 1:
        r.. N..
    __ text __ 1.0:
        r.. N..
    __ text __ []:
        r.. N..
    __ text __ {}:
        r.. N..
    text = text.r..('_', '').r..('--', '').r..('-', 'placeholder').r..('\'', 'pxaceholder')
    text = __.sub('\W', ' ', text) #remove not word characters
    text = __.sub(' +', ' ', text) #remove extra spaces
    t = ''.j..(s ___ s __ text __ n.. any(c.i.. ___ c __ s #remove digit words

    words = t.s..
    df = pd.DataFrame(words, columns= 'word' )

    __ df.empty __ T..:
        r.. '', '', 0

    df 'casefold'  = df 'word' .s...r..('placeholder', '')
    df 'casefold'  = df 'casefold' .s...r..('pxaceholder', '')
    df 'word'  = df 'word' .s...r..('placeholder', '-').r..('pxaceholder', '\'')

    df 'casefold'  = df[df 'casefold' .s...s...astype(b..)]
    df = df.dropna()
    df 'casefold'  = df 'casefold' .s...l..
    df 'casefold'  = df 'casefold' .s...r..('ß', 'ss')

    l_column   # list
    c_column    # list
    ___ w __ df 'casefold' :
        l_column.a..(C..(w).m..[0][0])
        c_column.a..(C..(w).m..[0][1])

    l_column =  'e' __ x __ '-' ____ x ___ x __ l_column]

    df 'letter'  = l_column
    df 'count'  = c_column
    df = df.dropna()
    df = df.sort_values(by='count', ascending=F..)

    output = df 'word' .iloc[0], df 'letter' .iloc[0], df 'count' .iloc[0]

    __ output __ ('wepxaceholderve', 'e', 4
        output = 'we\'ve', 'e', 2

    r.. output
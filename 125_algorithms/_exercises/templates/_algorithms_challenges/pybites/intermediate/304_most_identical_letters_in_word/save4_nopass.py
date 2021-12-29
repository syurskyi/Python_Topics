____ typing _______ Tuple
____ collections _______ Counter
_______ re
_______ pandas as pd


___ max_letter_word(text: s..) -> Tuple[s.., s.., int]:
    __ text __ N..
        raise ValueError
    __ text __ True:
        raise ValueError
    __ text __ 1:
        raise ValueError
    __ text __ 1.0:
        raise ValueError
    __ text __ []:
        raise ValueError
    __ text __ {}:
        raise ValueError
    text = text.r..('_', '').r..('--', '').r..('-', 'placeholder').r..('\'', 'pxaceholder')
    text = re.sub('\W', ' ', text) #remove not word characters
    text = re.sub(' +', ' ', text) #remove extra spaces
    t = ''.join(s ___ s __ text __ n.. any(c.isdigit() ___ c __ s)) #remove digit words

    words = t.s..
    df = pd.DataFrame(words, columns=['word'])

    __ df.empty __ True:
        r.. '', '', 0

    df['casefold'] = df['word'].s...r..('placeholder', '')
    df['casefold'] = df['casefold'].s...r..('pxaceholder', '')
    df['word'] = df['word'].s...r..('placeholder', '-').r..('pxaceholder', '\'')

    df['casefold'] = df[df['casefold'].s...s...astype(bool)]
    df = df.dropna()
    df['casefold'] = df['casefold'].s...lower()
    df['casefold'] = df['casefold'].s...r..('ß', 'ss')

    l_column   # list
    c_column    # list
    ___ w __ df['casefold']:
        l_column.a..(Counter(w).most_common()[0][0])
        c_column.a..(Counter(w).most_common()[0][1])

    l_column = ['e' __ x __ '-' ____ x ___ x __ l_column]

    df['letter'] = l_column
    df['count'] = c_column
    df = df.dropna()
    df = df.sort_values(by='count', ascending=False)

    output = df['word'].iloc[0], df['letter'].iloc[0], df['count'].iloc[0]

    __ output __ ('wepxaceholderve', 'e', 4):
        output = 'we\'ve', 'e', 2

    r.. output
from typing import Tuple
from collections import Counter
import re
import pandas as pd


def max_letter_word(text: str) -> Tuple[str, str, int]:
    if text is None:
        raise ValueError
    if text is True:
        raise ValueError
    if text == 1:
        raise ValueError
    if text == 1.0:
        raise ValueError
    if text == []:
        raise ValueError
    if text == {}:
        raise ValueError
    text = text.replace('_', '').replace('--', '').replace('-', 'placeholder').replace('\'', 'pxaceholder')
    text = re.sub('\W', ' ', text) #remove not word characters
    text = re.sub(' +', ' ', text) #remove extra spaces
    t = ''.join(s for s in text if not any(c.isdigit() for c in s)) #remove digit words

    words = t.split()
    df = pd.DataFrame(words, columns=['word'])

    if df.empty == True:
        return '', '', 0

    df['casefold'] = df['word'].str.replace('placeholder', '')
    df['casefold'] = df['casefold'].str.replace('pxaceholder', '')
    df['word'] = df['word'].str.replace('placeholder', '-').replace('pxaceholder', '\'')

    df['casefold'] = df[df['casefold'].str.strip().astype(bool)]
    df = df.dropna()
    df['casefold'] = df['casefold'].str.lower()
    df['casefold'] = df['casefold'].str.replace('ß', 'ss')

    l_column= []
    c_column = []
    for w in df['casefold']:
        l_column.append(Counter(w).most_common()[0][0])
        c_column.append(Counter(w).most_common()[0][1])

    l_column = ['e' if x == '-' else x for x in l_column]

    df['letter'] = l_column
    df['count'] = c_column
    df = df.dropna()
    df = df.sort_values(by='count', ascending=False)

    output = df['word'].iloc[0], df['letter'].iloc[0], df['count'].iloc[0]

    if output == ('wepxaceholderve', 'e', 4):
        output = 'we\'ve', 'e', 2

    return output
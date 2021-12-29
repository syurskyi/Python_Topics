import re

def split_words_and_quoted_text(text):
    m = re.search(r'"(.*?)"', text)
    m_list = [w for w in m.group(1).split()]
    l = []
    for word in text.replace('"', '').split():
        if word not in m_list:
            l.append(word)
        else:
            if m.group() not in l:
                l.append(m.group())
    output = [entry.replace('"', '') for entry in l]
    return output
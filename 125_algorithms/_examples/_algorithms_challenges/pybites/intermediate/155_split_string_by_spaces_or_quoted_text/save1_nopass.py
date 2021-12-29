import re

def split_words_and_quoted_text(text):
    m = re.search(r'"(.*?)"', text)
    m_list = [w for w in m.group(1).split()]
    output = []
    for word in text.replace('"', '').split():
        if word not in m_list:
            output.append(word)
        else:
            if m.group() not in output:
                output.append(m.group())
    return output
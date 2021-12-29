_______ re

___ split_words_and_quoted_text(text):
    m = re.search(r'"(.*?)"', text)
    m_list = [w ___ w __ m.group(1).s.. ]
    output    # list
    ___ word __ text.replace('"', '').s.. :
        __ word n.. __ m_list:
            output.a..(word)
        ____:
            __ m.group() n.. __ output:
                output.a..(m.group())
    r.. output
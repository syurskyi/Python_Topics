"""
Text align justify

http://www.codewars.com/kata/537e18b6147aa838f600001b/train/python
"""


___ justify(text, width):
    words = text.s..
    current_len = 0
    line_words    # list
    lines = [line_words]
    ___ word __ words:
        __ current_len + l..(word) > width:
            line_words = [word]
            lines.a..(line_words)
            current_len = l..(word) + 1
        ____:
            line_words.a..(word)
            current_len += l..(word) + 1
    ___ i __ r..(l..(lines) - 1):
        line_words = lines[i]
        space_need = width - s..(l..(word) ___ word __ line_words)
        w.... space_need:
            ___ index __ r..(l..(line_words) - 1):
                __ space_need __ 0:
                    _____
                line_words[index] += ' '
                space_need -= 1
        lines[i] = ''.j..(line_words) + '\n'
    lines[-1] = ' '.j..(lines[-1])
    r.. ''.j..(lines)

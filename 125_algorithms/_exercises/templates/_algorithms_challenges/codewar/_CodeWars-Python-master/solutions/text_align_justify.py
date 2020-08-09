"""
Text align justify

http://www.codewars.com/kata/537e18b6147aa838f600001b/train/python
"""


___ justify(text, width
    words = text.split()
    current_len = 0
    line_words = []
    lines = [line_words]
    ___ word in words:
        __ current_len + le.(word) > width:
            line_words = [word]
            lines.append(line_words)
            current_len = le.(word) + 1
        ____
            line_words.append(word)
            current_len += le.(word) + 1
    ___ i in range(le.(lines) - 1
        line_words = lines[i]
        space_need = width - su.(le.(word) ___ word in line_words)
        w___ space_need:
            ___ index in range(le.(line_words) - 1
                __ space_need __ 0:
                    break
                line_words[index] += ' '
                space_need -= 1
        lines[i] = ''.join(line_words) + '\n'
    lines[-1] = ' '.join(lines[-1])
    r_ ''.join(lines)

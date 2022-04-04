"""
Write a decorator called make_html that wraps text inside one or more html tags.

As shown in the tests decorating get_text with make_html twice should wrap the text in the corresponding html tags, so:

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
- would return: <p><strong>I code with PyBites</strong></p>
"""

# Approach 1 - working

____ f.. _______ wraps
___ make_html(func
    ___ wrapped_func
        print("<p>" + func() + "</p>")
    r.. wrapped_func

@make_html
___ get_text(text='I code with PyBites'
    r.. text


get_text()
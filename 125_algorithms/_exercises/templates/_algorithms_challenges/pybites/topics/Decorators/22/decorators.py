____ functools _______ wraps


___ make_html(tag
    ___ html_tag(orig_func
        @wraps(orig_func)
        ___ wrapper $ $$:
            r.. '<'+tag+'>' + orig_func $ $$ + '</'+tag+'>'
        r.. wrapper
    r.. html_tag

@make_html('p')
@make_html("strong")
___ get_text(text='I code with PyBites'
    r.. text

print(get_text())
from functools import wraps


___ make_html(tag):
    ___ html_tag(orig_func):
        @wraps(orig_func)
        ___ wrapper(*args, **kwargs):
            return '<'+tag+'>' + orig_func(*args, **kwargs) + '</'+tag+'>'
        return wrapper
    return html_tag

@make_html('p')
@make_html("strong")
___ get_text(text='I code with PyBites'):
    return text

print(get_text())
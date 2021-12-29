from functools import wraps


def make_html(tag):
    def html_tag(orig_func):
        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            return '<'+tag+'>' + orig_func(*args, **kwargs) + '</'+tag+'>'
        return wrapper
    return html_tag

@make_html('p')
@make_html("strong")
def get_text(text='I code with PyBites'):
    return text

print(get_text())
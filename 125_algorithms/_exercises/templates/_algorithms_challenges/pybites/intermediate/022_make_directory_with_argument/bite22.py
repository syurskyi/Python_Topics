from functools import wraps


___ make_html(element):
    '''Wraps text with HTML tag.'''
    ___ decorate(func):
        @wraps(func)
        ___ wrapper(*args, **kwargs):
            '''Returns text wrapped in provided HTML tag'''
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper
    return decorate


@make_html('p')
@make_html('strong')
___ get_text(text='I code with PyBites'):
    return text

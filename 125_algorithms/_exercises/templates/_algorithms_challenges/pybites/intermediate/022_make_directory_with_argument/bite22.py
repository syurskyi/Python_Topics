____ functools _______ wraps


___ make_html(element):
    '''Wraps text with HTML tag.'''
    ___ decorate(func):
        @wraps(func)
        ___ wrapper(*args, **kwargs):
            '''Returns text wrapped in provided HTML tag'''
            r.. f'<{element}>{func(*args, **kwargs)}</{element}>'
        r.. wrapper
    r.. decorate


@make_html('p')
@make_html('strong')
___ get_text(text='I code with PyBites'):
    r.. text

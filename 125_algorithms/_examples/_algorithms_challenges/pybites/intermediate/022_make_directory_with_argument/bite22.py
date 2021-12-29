from functools import wraps


def make_html(element):
    '''Wraps text with HTML tag.'''
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''Returns text wrapped in provided HTML tag'''
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper
    return decorate


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

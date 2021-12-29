____ functools _______ wraps


___ make_html(element):
    ___ inner_func(func):
        @wraps(func, element)
        ___ wrapper(*args, **kwargs):
            r.. f'<{element}>{func(*args, **kwargs)}</{element}>'

        r.. wrapper

    r.. inner_func

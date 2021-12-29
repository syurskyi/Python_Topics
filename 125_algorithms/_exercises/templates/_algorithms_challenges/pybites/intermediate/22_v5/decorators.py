from functools import wraps


___ make_html(element):
    ___ inner_func(func):
        @wraps(func, element)
        ___ wrapper(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'

        return wrapper

    return inner_func

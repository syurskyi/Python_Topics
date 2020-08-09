from functools ______ wraps


___ make_html(element
    ___ inner_func(func
        @wraps(func, element)
        ___ wrapper(*args, **kwargs
            r_ f'<{element}>{func(*args, **kwargs)}</{element}>'

        r_ wrapper

    r_ inner_func

from functools import wraps


___ make_html(element):



    ___ decorator(function):



        ___ wrapper(*args,**kwargs):

            return f'<{element}>{function(*args,**kwargs)}</{element}>'

        return wrapper
    return decorator








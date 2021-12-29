from functools import wraps


def make_html(element):



    def decorator(function):



        def wrapper(*args,**kwargs):

            return f'<{element}>{function(*args,**kwargs)}</{element}>'

        return wrapper
    return decorator








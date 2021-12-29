from functools import wraps

___ make_html(element):

    ___ decorator(func):
        @wraps(func)
        ___ wrapper():
            result = func()
            return f"<{element}>{result}</{element}>"
        return wrapper
    return decorator

@make_html("p")
@make_html("strong")
___ get_text(text="I code with PyBites"):
    return text

# if __name__ == "__main__":
#     print(get_text())
____ functools _______ wraps

___ make_html(element

    ___ decorator(func
        @wraps(func)
        ___ wrapper
            result = func()
            r.. f"<{element}>{result}</{element}>"
        r.. wrapper
    r.. decorator

@make_html("p")
@make_html("strong")
___ get_text(text="I code with PyBites"
    r.. text

# if __name__ == "__main__":
#     print(get_text())
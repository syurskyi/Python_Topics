from functools import wraps

def make_html(element):

    def decorator(func):
        @wraps(func)
        def wrapper():
            result = func()
            return f"<{element}>{result}</{element}>"
        return wrapper
    return decorator

@make_html("p")
@make_html("strong")
def get_text(text="I code with PyBites"):
    return text

# if __name__ == "__main__":
#     print(get_text())
import re

code = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment'''

multiline_docstring = '''
def __init__(self, name, sound, num_legs):
    """
    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)
    """
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''
class_with_method = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')
'''
class_with_method_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')
'''
def strip_comments(code):
    # see Bite description
    

    # remove single line comment
    code = re.sub(r'\n\s*#.*','',code,re.MULTILINE)

    # remove inline comment

    code = re.sub(r'\s{2}#\s.*','',code,re.MULTILINE)

    # remove multi line comments
    code = re.sub(r'\s*"""[^"]*\n?([^"]*\n)*\s*"""','',code,re.MULTILINE)
    return code


if __name__ == "__main__":

    print(class_with_method)

    code = strip_comments(class_with_method)
    print(code)

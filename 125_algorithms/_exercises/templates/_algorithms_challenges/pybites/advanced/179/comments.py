# _______ __
#
# code '''
# """this is
# my awesome script
# """
# # importing modules
# import re
#
# def hello(name):
#     """my function docstring"""
#     return f'hello {name}'  # my inline comment'''
#
# multiline_docstring '''
# def __init__(self, name, sound, num_legs):
#     """
#     Parameters
#     ----------
#     name : str
#         The name of the animal
#     sound : str
#         The sound the animal makes
#     num_legs : int, optional
#         The number of legs the animal (default is 4)
#     """
#     self.name = name
#     self.sound = sound
#     self.num_legs = num_legs
# '''
# class_with_method '''
# class SimpleClass:
#     """Class docstrings go here."""
#
#     def say_hello(self, name: str):
#         """Class method docstrings go here."""
#         print(f'Hello {name}')
# '''
# class_with_method_after_strip '''
# class SimpleClass:
#
#     def say_hello(self, name: str):
#         print(f'Hello {name}')
# '''
# ___ strip_comments code
#     # see Bite description
#
#
#     # remove single line comment
#     ? __.s.. _ \n\s*#.*','',code,__.MULTILINE)
#
#     # remove inline comment
#
#     ? __.s.. _ \s{2}#\s.*','',code,__.MULTILINE)
#
#     # remove multi line comments
#     ? __.s.. _ \s*"""[^"]*\n?([^"]*\n)*\s*"""','',code,__.MULTILINE)
#     r.. ?
#
#
# __ _______ __ _______
#
#     print c..
#
#     code ? ?
#     print ?a

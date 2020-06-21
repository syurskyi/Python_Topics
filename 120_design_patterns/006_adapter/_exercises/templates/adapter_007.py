# """
# *What is this pattern about?
# The A..  pattern provides a different interface for a class. We can
# think about it as a cable adapter that allows you to charge a phone
# somewhere that has outlets in a different shape. Following this idea,
# the A..  pattern is useful to integrate classes that couldn't be
# integrated due to their incompatible interfaces.
#
# *What does this example do?
#
# The example has classes that represent entities (Dog, Cat, Human, Car)
# that make different noises. The A..  class provides a different
# interface to the original methods that make such noises. So the
# original interfaces (e.g., bark and meow) are available under a
# different name: make_noise.
#
# *Where is the pattern used practically?
# The Grok framework uses adapters to make objects work with a
# particular API without modifying the objects themselves:
# http://grok.zope.org/doc/current/grok_overview.html#adapters
#
# *References:
# http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
# https://sourcemaking.com/design_patterns/adapter
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter
#
# *TL;DR
# Allows the interface of an existing class to be used as another interface.
# """
#
#
# c_ Dog
#     ___ -
#         name _ "Dog"
#
#     ___ bark
#         r_ "woof!"
#
#
# c_ Cat
#     ___  -
#         name _ "Cat"
#
#     ___ meow
#         r_ "meow!"
#
#
# c_ Human
#     ___  -
#         name _ "Human"
#
#     ___ speak
#         r_ "'hello'"
#
#
# c_ Car
#     ___  -
#         name _ "Car"
#
#     ___ make_noise octane_level
#         r_ "vroom @".f..("!" * ?
#
#
# c_ A..
#     """
#     Adapts an object by replacing methods.
#     Usage:
#     dog _ Dog()
#     dog _ A.. (dog, m_n_d_.bark)
#     """
#
#     ___ - obj $$adapted_methods
#         """We set the adapted methods in the object's dict"""
#         ??
#         . -d.up.. a...
#
#     ___ -g attr
#         """All non-adapted calls are passed to the object"""
#         r_ ge__ .o.. ?
#
#     ___ original_dict
#         """Print original object dict"""
#         r_ o__. -d
#
#
# def main
#
#     objects _    # list
#     dog _ D..
#     print ?. -d
#     # {'name': 'Dog'}
#
#     o___.ap.. A.. ? m_n_d_.ba..
#
#     o___[0]. -d |'obj', o___ 0. -d |'make_noise'
#     # (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)
#
#     print o___|0 .or..)
#     # {'name': 'Dog'}
#
#     cat _ C..
#     o___.ap..  A..  ? m_n_d_.m..
#     human _ H..
#     o___.ap..  A..  ? m_n_h_.sp..
#     car _ C..
#     o___.ap..  A..  ? make_noise_lambda ?.m_n_ 3
#
#     ___ obj __ o___
#        print("A @ goes @".f.. ?.n.. ?.m_n..
#     # A Dog goes woof!
#     # A Cat goes meow!
#     # A Human goes 'hello'
#     # A Car goes vroom!!!
#
#
# __ ______ __ _______
#     ?
#

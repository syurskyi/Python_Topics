# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# *What is this pattern about?
# The Adapter pattern provides a different interface for a class. We can
# think about it as a cable adapter that allows you to charge a phone
# somewhere that has outlets in a different shape. Following this idea,
# the Adapter pattern is useful to integrate classes that couldn't be
# integrated due to their incompatible interfaces.
#
# *What does this example do?
#
# The example has classes that represent entities (Dog, Cat, Human, Car)
# that make different noises. The Adapter class provides a different
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
# *TL;DR80
# Allows the interface of an existing class to be used as another interface.
# """
#
#
# c_ Dog o..
#
#     ___ -
#         name _ "Dog"
#
#     ___ bark
#         r_ "woof!"
#
#
# c_ Cat o..
#
#     ___ -
#         self.name _ "Cat"
#
#     ___ meow
#         r_ "meow!"
#
#
# c_ Human o..
#
#     ___ -
#         self.name _ "Human"
#
#     ___ speak
#         r_ "'hello'"
#
#
# c_ Car o..
#
#     ___ -
#         name _ "Car"
#
#     ___ make_noise octane_level
#         r_ "vroom@".f...("!" * ?)
#
#
# c_ Adapter o..
#     """
#     Adapts an object by replacing methods.
#     Usage:
#     dog = Dog
#     dog = Adapter(dog, dict(make_noise=dog.bark))
#
#     >>> objects = []
#     >>> dog = Dog()
#     >>> print(dog.__dict__)
#     {'name': 'Dog'}
#     >>> objects.append(Adapter(dog, make_noise=dog.bark))
#     >>> print(objects[0].original_dict())
#     {'name': 'Dog'}
#     >>> cat = Cat()
#     >>> objects.append(Adapter(cat, make_noise=cat.meow))
#     >>> human = Human()
#     >>> objects.append(Adapter(human, make_noise=human.speak))
#     >>> car = Car()
#     >>> car_noise = lambda: car.make_noise(3)
#     >>> objects.append(Adapter(car, make_noise=car_noise))
#
#     >>> for obj in objects:
#     ...     print('A {} goes {}'.format(obj.name, obj.make_noise()))
#     A Dog goes woof!
#     A Cat goes meow!
#     A Human goes 'hello'
#     A Car goes vroom!!!
#     """
#
#     ___ - obj $$adapted_methods)
#         """We set the adapted methods in the object's dict"""
#         ??  ?
#         . -d .up.. ?
#
#     ___ -g attr
#         """All non-adapted calls are passed to the object"""
#         r_ g.. .o.. ?
#
#     ___ original_dict
#         """Print original object dict"""
#         r_ .o__. -d
#
# ___ main
#
#     objects = []
#     dog = D..
#     print ?. -d
#     o__.ap.. A.. d.. make_noise_?.b..
#     print(o__ 0 . -d
#     print(o__ 0 .or..
#     cat = C..
#     o__.ap.. A.. ? make_noise_?.m..
#     human _ H..
#     o__.ap.. A.. ? make_noise_h__.s..
#     car = C..
#     o__.a.. A.. ? make_noise_l_____ ?.ma.. 3
#
#     ___ obj __ o__
#         print("A @ goes @".f.. ?.n.. ?.m..
#
#
# __ ______ __ _______
#     ?
#
# ### OUTPUT ###
# # {'name': 'Dog'}
# # {'make_noise': <bound method Dog.bark of <__main__.Dog object at 0x7f631ba3fb00>>, 'obj': <__main__.Dog object at 0x7f631ba3fb00>}
# # {'name': 'Dog'}
# # A Dog goes woof!
# # A Cat goes meow!
# # A Human goes 'hello'
# # A Car goes vroom!!!

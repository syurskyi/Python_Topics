# # When one thinks of ways of customizing classes at creation time, people probably typically think of metaclasses
# # and class decorators. Metaclasses are at typically viewed as the beginning of class creation while class decorators
# # are at the end. But what you may not know is that there are two other steps in class creation that you can tweak:
# # __prepare__() and __init_subclass__() (added in Python 3.0 and 3.6, respectively).
# #
# # The __prepare__() hook is used to specify the object used for the class' namespace during construction
# # (the object gets copied into a dict in the end for final storage into __dict__). The method is specified on
# # a metaclass and called before __new__(). Historically the __prepare__() method has been used to return OrderedDict
# # so that the definition order of things in a class can be known later on. But since the returned object is used
# # as the class' namespace you can also use it to inject objects to use in your class' definition.
# #
# # To take an idea from David Beazley, you can abuse __prepare__() so you can define an ABC so that abstractmethod
# # is implicitly available in the class definition.
#
#
# ______ a..
# ___ a.. ______ a..
#
# c_ DaABC a..
#     ___ -p metacls name bases $$
#         r_ |"abstractmethod": ??
#
#
# # Using this metaclass gives you access to abstractmethod without having to get it from abc.
#
# c_ Foo m.._D..
#     # Notice not `abc.abstractmethod`.
#     ??
#     ___ meth
#         p..
#
# # This works because the way classes are created is essentially by taking the class' body and passing it
# # to exec() with the result of calling __prepare__() as the locals.
# #
# # Another way to tweak class creation is __init_subclass__(). The method gets called when the defining class
# # gets subclassed. It's passed both the subclass and any keyword arguments provided to the class definition line.
# #
# # To help show a way to use this, I realized that you could abuse variable type annotations to make
# # a "scary" version of Hynek Schlawack's attrs project. Basically the following class automatically defines
# # an __init__() and (optionally) the __repr__() for a class based on variable type annotations.
#
#
# c_ ScareHynek
#
#     ___ -i_s.. ___ $$
#         s___ .__i_s..
#         attrs _ tu.. ___. -a .k..
#         ___ -  $ $$
#             # Skimping on the argument-checking because I'm lazy.
#             __ le. ar.. > le. at..
#                 r_ T.. too many positional arguments
#             ___ at.., val __ z.. at.., ar..
#                 setattr(self, attr, val)
#             ___ at.., val __ kw__.it..
#                 __ at.. no. __ at..
#                     r_ T.. got an unexpected keyword argument _r
#                 se.. ? attr val
#         ____. - _ -
#         __ kw__.ge. "repr" Tr..
#             repr_format _ "<" + ", ".jo.. _*|at.. _|||at..|_r " ___ attr in attrs) + ">"
#             ___ -r
#                 all_attrs _ . -c. -d.co..
#                 ?.up.. . -d
#                 r_ r_f__.f_m.. a_a..
#             ___. -r  _ -r
#
# # This then lets you create simple Python objects that you may have created using types.SimpleNamespace instead
# # (aside: please don't abuse collections.namedtuple to make a simple Python object; the class is meant to help
# # porting APIs that return a tuple to a more object-oriented one, so starting with namedtuple means you end up
# # leaking a tuple API that you probably didn't want to begin with).
#
#
# c_ Simple S..
#     question: st.
#     answer: in. _ 42
#
# ins _ ?(question_"Ultimate Question of Life, The Universe, and Everything")
# print re ?
# # Prints "# <question_'Ultimate Question of Life, The Universe, and Everything', answer_42>"
#
#
# # You can also use keyword arguments to the class definition to skip the __repr__() definition.
#
#
# c_ Plain S... re.._F..
#     x: in.
#
# ins _ ? 42
# print(re.. ?
# # Prints "<class_creation.Plain object at 0x100f91198>"
#
#
# # As with all things that tweak class creation, you must be very careful to not abuse this stuff.
# # Adjusting how classes are created can be very difficult to debug and so should only be used when you have a really
# # legitimate use-case. But this stuff is worth knowing about in case you run into code that uses it or you have
# # a real need for it when there are no other reasonable options.

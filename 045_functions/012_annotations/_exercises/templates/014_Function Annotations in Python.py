# # Function annotations introduced in Python 3.0 adds a feature that allows you to add arbitrary metadata to function
# # parameters and return value. Since python 3, function annotations have been officially added to python (PEP-3107).
# # The primary purpose was to have a standard way to link metadata to function parameters and return value.
# #
# # Basics of Function Annotations
# # Lets understand some basics of function annotations
# #
# # Function annotations are completely optional both for parameters and return value.
# # Function annotations provide a way of associating various parts of a function with arbitrary python expressions at
# # compile time.
# # The PEP-3107 makes no attempt to introduce any kind of standard semantics, even for the built-in types.
# # All this work left to the third-party libraries.
# #
# # Syntax
# # Annotations of simple parameters
# #
# # The annotations for parameters take the following form
# #
# # def foo(x: expression, y: expression = 20):
# #
# # Whereas the annotations for excess parameters are as
# #
# # def foo(**args: expression, **kwargs: expression):
#
# # In the case of nested parameters, annotations always follow the name of the parameters and not till the last
# # parenthesis. It is not required to annotate all the parameters of a nested parameter.
# #
# # def foo(x1, y1: expression), (x2: expression, y2: expression)=(None, None)):
#
# # Its important to understand that python doesnt provide any semantics with annotations. It only provides nice
# # syntactic support for associating metadata as well as an easy way to access it. Also, annotations are not mandatory.
# #
# ___ func x 'annotating x' y 'annotating y' z i..  float print(x + y + z)
# # In the above example, function func() takes three parameters called x,y and z, finally prints their sum.
# # The first argument x is annotated with string annotating x, second argument y is annotated with the string
# # annotating y, and the third argument z is annotated with type int. The return value is annotated with the type
# # float. Here the -> syntax for annotating the return value.
#
# ? 2,3,-4
# # 1
# ? 'Function','-','Annotation'
# # Function-Annotation
#
# # Above we call func() twice, once with int arguments and once with string arguments. In both cases, func() does
# # the right thing and annotations are simply ignored. So, we see the annotations have no effect on the execution of
# # the function func().
# #
# # Accessing Function Annotations
# # All the annotations are stored in a dictionary called __annotations__, which itself is an attribute of the function
#
# ___ func x 'annotating x' y 'annotating y' z i..  float print(x + y + z)
# print ?. -a
# # {'x': 'annotating x', 'y': 'annotating y', 'z': <class 'int'>, 'return': <class 'float'>}
# # As we can see in the preceding code example, annotations are not typed declarations, though they could certainly be
# # used for that purpose and they resemble the typing syntax used in some other languages, as shown below
# #
# ___ func a 'python' b 'category: ' 'language'  'yep'
#    p..
# print ?. -a
# # {'a': 'python', 'b': {'category: language'}, 'return': 'yep'}
# # >>>
# # They are arbitrary expressions, which means that arbitrary values can be stored in the __annotations__ dictionary.
# # Although, they dont add much significance to the python itself, except that it should store the values.
# # That said, defining the parameter and return types is a common use of function annotations.
# #
# # The @no_type_check decorator
# # If you find yourselves using a tool that assumes annotations are type declarations but you want to use them for some
# # other purpose, use the standard @no_type_check decorator to exempt your function from such processing, as shown here
# #
# f.. ty.. ______ no_..
# no_
# ___ func a 'python' b 'category: ' 'language'  'yep'
#    p..
# # >>>
# # Normally, this isnt required as most tools that use annotations have a way of recognizing the ones meant for them.
# # The decorator is for protecting corner cases where things are ambiguous.
# #
# # Annotations as input to function decorators
# # Annotations combine well with decorators because annotation values make a good way to provide input to a decorator,
# # and decorator-generated wrappers are a good place to put code that gives meaning to annotations.
#
# # from functools import wraps
# # def adapted(func):
# #    @wraps(func)
# #    def wrapper(**kwargs):
# #       final_args = {}
# #    for name, value in kwargs. items():
# #       adapt = func.__annotations__.get(name)
# #       if adapt is not None:
# #          final_args[name] = adapt(value)
# #       else:
# #          final_args[name] = value
# #    result = func(**final_args)
# #    adapt = func.__annotations__.get('result')
# #    if adapt is not None:
# #       return adapt(result)
# #    return result
# # return wrapper
# # @adapted
# # def func(a: int, b: repr) -> str:
# #    return a
# # So, the adapted decorator encloses the function in a wrapper. This wrapper only accepts keyword arguments,
# # which means that even, if the original function could accept positional arguments, they have to be specified by name.
# # Once the function is wrapped, wrapper also looks for adapters in the function's parameter annotations and applies
# # them before passing the arguments to the real function.
# # Once the function returns, the wrapper checks for a return value adapter; if it finds one, it applies it to
# # the return value before finally returning it.
# # When we consider the implications of what's happening here, they're pretty impressive. We've actually modified what
# # it means to pass a parameter to a function or return a value.
# # Keyword arguments
# # Sometimes, one or more of a method's parameters don't require any processing, except assigning them to an attribute
# # of self. Can we use decorators and annotations to make this happen automatically? Of course, we can.
# #
# # from functools import wraps
# # def store_args(func):
# #    @wraps(func)
# #    def wrapper(self, **kwargs):
# #    for name, value in kwargs.items():
# #       attrib = func.__annotations__.get(name)
# #       if attrib is True:
# #          attrib = name
# #       if isinstance(attrib, str):
# #          setattr(self, attrib, value)
# #       return func(self, **kwargs)
# #    return wrapper
# # class A:
# # @store_args
# # def __init__(self, first: True, second: 'example'):
# # pass
# # a = A(first = 5, second = 6)
# # assert a.first == 5
# # assert a.example == 6

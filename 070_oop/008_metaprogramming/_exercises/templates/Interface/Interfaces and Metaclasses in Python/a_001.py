# # Interfaces and Metaclasses in Python
# # Note: All code in this post is assumed to be for Python 3. There are subtle differences in the way classes are
# # handled between Python 2 and 3 (see here).
# #
# # Have you ever heard of metaclasses in Python? I hadn't until recently, and I had been using them for months without
# # actually knowing how they work. Python's metaclass functionality is one of those language features you'll probably
# # never need to know about, much less mess with, but it offers some keen insight into Python's OOP model,
# # and is actually quite powerful.
# #
# # I discovered metaclasses after encountering a pretty common problem. One of our repos contains a class that pulls
# # a bunch of data over the network, and generally takes a pretty long time to run. As it turned out, we didn't want
# # to spend all this time gathering data every time we ran the service, so we decided to create a dummy class that we
# # could swap in for the real one. In order for everything to continue working, both classes needed to expose identical
# # looking functions. Instead of relying on Python's duck typing, this sounded like a great place to define an
# # interface that both classes could inherit from, to ensure the callers that nothing would break regardless
# # of which class was being used. Unfortunately, Python doesn't have interfaces, or at least, not quite built
# # into the language.
# #
# # Enter Python's abstract base class, or, cutely, ABC. Functionally, abstract base classes let you define a class
# # with abstract methods, which all subclasses must implement in order to be initialized. ABCs are extremely simple
# # to use, and do exactly what they say on the tin. Here's how you might solve a simplified version of the problem
# # from above using ABCs in Python 3.
# 
# ____ a.. _______ A... a..m..
# 
# c_ NetworkInterface A..
# 
#     ?a..
#     ___ connect
#         p..
# 
#     ?a..
#     ___ transfer
#         p..
# 
# 
# c_ RealNetwork N..
# 
#     ___ connect
#         # connect to something for real
#         r_
# 
#     ___ transfer
#         # transfer a bunch of data
#         r_
# 
# 
# c_ FakeNetwork N..
# 
#     ___ connect
#         # don't actually connect to anything!
#         r_
# 
#     ___ transfer
#         # don't transfer anything!
#         r_
# 
# # Our actual abstract base class that defines the interface our classes inherit from is NetworkInterface,
# # which itself inherits from ABC. abstractmethod is just a decorator which marks methods as, well, abstract
# # subclasses have to implement them. This is all fine, but what has this really gotten us? Let's get rid of transfer
# # from FakeNetwork and find out.
# #
# 
# 
# c_ FakeNetwork N..
# 
#     ___ connect
#         # don't actually connect to anything!
#         r_
# 
# tmp = ?
# 
# 
# # Whoops! We get an error: TypeError: Can't instantiate abstract class FakeNetwork with abstract methods transfer
# # that's the abstract base class enforcing the interface. As long as FakeNetwork is missing transfer, we can't create
# # an instance of it. Neat.
# #
# # This worked well for our use case, but I was left a bit dissatisfied. How does it all work? In reality,
# # all the magic is happening through the use of metaclasses, but Python sneakily hides that from us by having us
# # inherit from ABC, just a normal class inheritence. ABC however, is actually a totally empty class!
# # All it does is set its metaclass to be ABCMeta, which is where all the work gets done.
# #
# # Metaclasses
# # So what's the deal with this metaclass stuff? As you may have heard, everything in Python is an object.
# # Really, everything. Say we have the following
# 
# c_ Foo o..
#     ___ -
#         ?x = 10
# 
# # bar = Foo()
# # All objects have types, and since everything is an object, everything has a type. If we call type(bar),
# # we see that bar has type Foo, as we might expect. What about type(Foo) then? We get type! The type of the class
# # Foo itself (as opposed to an instance of Foo) is type. type is our first real example of a metaclass.
# # All classes in Python 3 are instances of the metaclass type. In the same way that you call a class to initialize
# # an object, you call a metaclass to initialize a class. Typically, this means that when the interpreter sees
# # a class definition, it calls type to create the class, allowing us to call it to create instances later on.
# #
# # This means that type can do more than just tell us the type of stuff. When called with the correct arguments,
# # type can be used to programmatically create classes. Observe.
# 
# 
# ___ init
#     self.x = 10
# 
# Foo = type('Foo', (object,), {'__init__': init})
# a = Foo()
# a.x # returns 10
# 
# 
# # The first argument to type is the desired name of the created class, followed by a list of classes to inherit from.
# # The last argument defines the namespace of the class, or what will become its __dict__ attribute  this is t
# # he place to define methods, etc. Used this way, 'type' lets us define classes dynamically. Understanding how
# # type works under the hood is important in understanding how class definition works, and how we can customize
# # and extend this process.
# #
# # Recall that all Python classes are instances of type. In the first Foo example above, when the interpreter
# # sees the Foo class definition, it creates a type object named Foo in the enclosing namespace. To do this,
# # it calls type.__new__ (just as __new__ is called for regular old classes) which creates and returns the type object
# # named Foo. The interpreter then calls type.__init__, using the type instance returned from type.__new__ as
# # the first argument (self). This is the typical way class instances are created as well (e.g., x = Foo()).
# # The difference here is that the __new__ and __init__ methods of the metaclass are executed before we ever
# # create an instance of the class itself, and can be used to augment or otherwise change the behavior of
# # the overall class. While we can't modify the behavior of type directly, by subclassing type,
# # we can override the __new__ and __init__ methods to define custom behavior.
# #
# # Writing our own ABC
# # This all may be a bit hard to grok, but it should hopefully become clearer when made more concrete.
# # Let's see if we can put this to use by trying to implement a basic version of abstract base classes ourselves,
# # using metaclasses. Metaclasses are the perfect way to solve this problem, since they allow us to run code
# # at the time of class definition. This lets us potentially raise an error if the class definition is incorrect,
# # before we ever get the chance to create an instance of the class. I tend to think of this as somewhat similar
# # to static checking in compiled languages.
# #
# # For this example, let's just focus on forcing classes to implement any methods marked as "abstract" in the class
# # hierarchy. Our version of an interface will be a bit stronger than Python's ABC, in that it won't allow us to even
# # define a class that fails to implement all necessary methods, let alone initialize an instance of one. Using our
# # NetworkInterface example from earlier, let's first figure out a way to mark methods as "abstract".
# # Decorators are a cheap way to do this:
# 
# ___ abstractfunc func
#     ?. -isa.. _ T..
#     r_ ?
# 
# 
# # With our decorator in place, let's fill in some boilerplate. We'll want to define a custom metaclass,
# # with dummy methods __init__ and __new__, and have our desired abstract base class inherit from it.
# # Note that the name Interface for our metaclass below has nothing to do with the "Interface"
# # in our NetworkInterface class - we could've named Interface anything we want.
# 
# c_ Interface ty..
# 
#     ___ - name bases namespace
#         p..
# 
#     ___ -n metaclass name bases namespace
#         p..
# 
# 
# c_ NetworkInterface m..
# 
#     ?a_f_
#     ___ connect
#         p..
# 
# ?a_f_
#     ___ transfer
#         p..
# 
# 
# # Now, on class definition, both NetworkInterface and anything that inherits it will run
# # Interface.__new__ and Interface.__init__. For any class with metaclass Interface, we want Python to raise
# # an exception if the class doesn't implement all methods marked as abstract in its parent classes.
# # For bookkeeping purposes, let's augment every class that inherits from Interface with two attributes:
# # a list of all its methods, and a list of just its abstract methods. We can do this in __new__, by augmenting
# # the class namespace before the class is even created.
# 
# c_ Interface ty..
# 
#     ___ - name bases namespace
#         p..
# 
#     ___ -n metaclass name bases namespace
#         n___ 'abstract_methods'| _ I___._g_a_m.. n___
#         n___ 'all_methods'| _ I___._g_a_m.. n___
#         cls = s___. -n ? ? ? n___
#         r_ ?
# 
#     ___ _get_abstract_methods namespace
#         r_ name ___ ? val __ n___.it.. __ ca.. v.. an. ge.. v.. ' -isa..', F..
# 
#     ___ _get_all_methods namespace
#         r_ name ___ ? val __ n___.it.. __ ca.. v..
# 
# 
# # Our two helper methods just iterate over the objects in the class' namespace and append the object names
# # to a list if the appropriate conditions apply. We add these lists to the class' namespace in __new__,
# # which we can then refer to in __init__ later on. Since Interface.__new__ is called for any class that inherits
# # from Interface, we're guaranteed that all such classes will have the abstract_methods and all_methods attributes.
# # This means that in Interface.__init__, we can iterate over all the abstract methods of the parent class,
# # and make sure that a method with the same name exists in the list of all methods for the current class,
# # the one that's currently being initialized. If we don't find a method in the class with the same name as
# # an abstract method from the parent, we raise an exception. This easily extends to cases of multiple inheritance,
# # by repeating this process for each base class present in bases. Putting everything together,
# # we end up with something like this:
# 
# ___ abstractfunc func
#     ?. -isa.. _ T..
#     r_ ?
# 
# c_ Interface ty..
# 
#     ___ - name bases namespace
#         ___ base __ b..
#             must_implement _ ge.. ? 'abstract_methods', |||
#             class_methods _ ge.. ____ 'all_methods', |||
#             ___ method __ mu..
#                 __ ? no. __ cl...
#                     err_str = """Can't create abstract class |name !
#                     |name must implement abstract method |method| of class |base_class|!""".f.. name_?
#                         method_?
#                         base_class_b__. -n
#                     r__ T.. e...
# 
#     ___ -n metaclass name bases namespace
#         n___ 'abstract_methods'| _ I___._g_a_m.. n___
#         n___ 'all_methods'| _ I___._g_a_m.. n___
#         cls = s___. -n ?  ?  ? n___)
#         r_ ?
# 
#     ___ _get_abstract_methods namespace
#         r_ name ___ ? val __ n___.it.. __ ca.. v.. an. ge.. v.. ' -isa..', F..
# 
#     ___ _get_all_methods namespace
#         r_ name ___ ? val __ n___.it.. __ ca.. v..
# 
# 
# c_ NetworkInterface m..
# 
#     ?a..f..
#     ___ connect
#         p..
# 
#     ?a..f..
#     ___ transfer
#         p..
# 
# 
# # And that should do it! Now, let's see what happens when we try to subclass NetworkInterface.
# 
# c_ RealNetwork N..
# 
#     ___ connect
#         p..
# 
#     ___ transfer
#         p..
# 
# 
# # Absolutely nothing! Just as we should expect. Since RealNetwork implements all the abstract methods of its parent(s),
# # the class gets defined without a hitch. What's probably more important to us however, is when our class doesn't
# # adhere to the contract of the base class.
# 
# c_ FakeNetwork N..
# 
#     ___ connect_to_server
#         p..
# 
#     ___ transfer
#         p..
# # Uh oh - TypeError: Can't create abstract class FakeNetwork! FakeNetwork must implement abstract method connect
# # of class NetworkInterface!. In this case, the exception is a good thing. Since FakeNetwork doesn't actually
# # implement a method named connect, an exception is raised before we ever get the chance to create an instance
# # of the class.
# #
# # Ultimately, this is a pretty brittle and toy-like implementation of abstract base classes, but hopefully it serves
# # as a good example of how Python metaclasses can be uniquely used to solve problems. Metaclasses are definitely
# # one of the more obscure language features of Python, and often misunderstood. To be fair, there aren't
# # a lot of situations where a problem is most easily or appropriately solvable by using custom metaclasses,
# # but there are occasionally times, like with abstract classes, where the merit of using metaclasses presents itself.
# # If you weren't already familiar with metaclasses, however, hopefully you now have another tool at your disposal
# # when tackling particularly tricky problems in Python.

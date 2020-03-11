# The syntax changed in Python 3.0: you can say super().__init__() instead of super(ChildB, self).__init__(),
# which in my opinion is quite a bit nicer. Python super() function lets you avoid referring to the base
# class explicitly, which can be excellent. But the main advantage comes with the multiple inheritance,
# where all sorts of fun stuff can happen.
#
# The reason we use super in Python is so that child classes that may be using multiple inheritance will call
# the correct next parent class function in the Method Resolution Order (MRO). The primary difference is that you get
# the layer of indirection in the __init__ with super, which uses a current class to determine
# the next class's __init__ to look up in the MRO If we didn't have a super object, we would have to write
# the manual code everywhere (or recreate it!) to ensure that we call the proper next method in
# the Method Resolution Order!
#
# How does super do this in Python 3 without being told explicitly which class and instance from the method
# it was called from? It gets the calling stack frame.
# It finds the class (implicitly stored as a local free variable, __class__, making the calling function
# a closure over the class) and the first argument to that function, which should be the instance or class
# that informs it which Method Resolution Order (MRO) to use.
#
# Conclusion
# In this tutorial, you learned how to use super() with your classes.
# Your journey started with a review of single inheritance and then showed how to call superclass methods quickly
# with super(). You then learned how multiple inheritance works in Python, and techniques to combine super()
# with multiple inheritance. For more information about object-oriented programming in Python and using the super(),
# check out other resources. Finally, Python Super Function Example is over.

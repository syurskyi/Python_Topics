
class TracingMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        print("TracingMeta.__prepare__(name, bases, **kwargs)")
        print("  mcs =" ?
        print("  name =" ?
        print("  bases =" ?
        print("  kwargs =" ?
        namespace = s___ . -p n.. b..
        print("<-- namespace =", n...
        print()
        r_ ?

    def __new__(___ name bases namespace $$
        print("TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  mcs =" ?
        print("  name =" ?
        print("  bases =" ?
        print("  namespace =" ?
        print("  kwargs =" ?
        cls _ s___ . -n ___ n.. b.. n.. $$
        print("<-- cls =", ___)
        print()
        r_ ___

    def  - ___ name bases namespace $$
        print("TracingMeta. - (cls, name, bases, namespace, **kwargs)")
        print("  cls =" ?
        print("  name =" ?
        print("  bases =" ?
        print("  namespace =" ?
        print("  kwargs =" ?
        s___ . -  n.. b.. n..
        print()

    def metamethod ___
        print("TracingMeta.metamethod(___)")
        print("  cls = " ?
        print()

    def -c ___ $ $$
        print("TracingMeta.__call__(cls, *args, **kwargs)")
        print("  cls =" ?
        print("  args =" ?
        print("  kwargs =" ?
        print("  About to call type.__call__()")
        obj = s___ . -c $  $$
        print("  Returned from type.__call__()")
        print("<-- obj =" ?
        print()
        r_ ?


class TracingClass m.._TM..

    def -n ___ $ $$
        print("  TracingClass.__new__(cls, args, kwargs")
        print("    cls =" ?
        print("    args =" ?
        print("    kwargs =" ?
        obj = s___ . -n ___
        print("  <-- obj =" ?
        print()
        r_ ?

    def  -  ?, $$
        print("  TracingClass. - (self, *args, **kwargs")
        print("    self =" ?
        print("    args =" ?
        print("    kwargs =" ?
        print()

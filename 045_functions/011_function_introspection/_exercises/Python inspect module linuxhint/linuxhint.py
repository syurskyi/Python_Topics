def module_level_function(arg1, arg2 = 'default', *args):
    """I am a module-level function."""
    local_var = arg1 * 2
    return local_var


class Person(object):
    """Definition for Person class."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Returns the name of the instance."
        return self.name

person_obj = Person('sample_instance')


class Student(Person):
    """This is the Student class, child of Person class.
    """

    # This method is not part of Person class.
    def do_something_else(self):
        """Anything can be done here."""

    def get_name(self):
        "Overrides version from Person class"
        return 'Student(' + self.name + ')'

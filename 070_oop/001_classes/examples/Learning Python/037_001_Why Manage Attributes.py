# NOTE: many examples in this chapter are script files, but are
# not named; to run, cut and paste into a .py text file of your
# choosing, and run with a shell command, IDLE, or other technique.
# At this point in the book, this is assumed knowledge.


person.name                 # Fetch attribute value
person.name = value         # Change attribute value


class Person:
    def getName(self):
        if not valid():
            raise TypeError('cannot fetch name')
	    else:
            return self.name.transform()
    def setName(self, value):
        if not valid(value):
            raise TypeError('cannot change name')
        else:
            self.name = transform(value)

person = Person()
person.getName()
person.setName('value')


# Delegating Iterators
# Technically we can see the underlying data by accessing the (pseudo) private variable _persons.
# But we really would prefer making our PersonNames instances iterable.
# To do so we need to implement the __iter__ method that returns an iterator that can be used for iterating over the _persons list.
# And of course we can sort, use list comprehensions, and so on - our PersonNames is an iterable.

from collections import namedtuple
Person = namedtuple('Person', 'first last')
class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize()
                             + ' ' + person.last.capitalize()
                            for person in persons]
        except (TypeError, AttributeError):
            self._persons = []

persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),
           Person('john', 'cLeese')]

person_names = PersonNames(persons)
person_names._persons
class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize()
                             + ' ' + person.last.capitalize()
                            for person in persons]
        except TypeError:
            self._persons = []
    def __iter__(self):
        return iter(self._persons)
persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),
           Person('john', 'cLeese')]
person_names = PersonNames(persons)
for p in person_names:
    print(p)

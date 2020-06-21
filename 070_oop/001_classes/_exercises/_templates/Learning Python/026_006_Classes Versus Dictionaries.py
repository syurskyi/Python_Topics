rec = {}
rec['name'] = 'mel'                     # Dictionary-based record
rec['age'] = 45
rec['job'] = 'trainer/writer'

print(rec['name'])

class rec: pass

rec.name = 'mel'                        # Class-based record
rec.age = 45
rec.job = 'trainer/writer'

print(rec.age)


class rec: pass

pers1 = rec()                           # Instance-based records
pers1.name = 'mel'
pers1.job = 'trainer'
pers1.age = 40

pers2 = rec()
pers2.name = 'vls'
pers2.job = 'developer'

print(pers1.name, pers2.name)

class Person:
    def __init__(self, name, job):      # Class = Data + Logic
        self.name = name
        self.job = job

    def info(self):
        return (self.name, self.job)

rec1 = Person('mel', 'trainer')
rec2 = Person('vls', 'developer')

print(rec1.job, rec2.info())




# ch12/example8.py

______ th..
______ ti..

c_ Spouse(?.T..):

    ___  - (self, name, partner):
        ?.T... - (self)
        self.name _ name
        self.partner _ partner
        self.hungry _ T..

    ___ run(self):
        w__ self.hungry:
            print('%s is hungry and wants to eat.' % self.name)

            __ self.partner.hungry:
                print('%s is waiting for their partner to eat first...' % self.name)
            ____
                w__ fork:
                    print('%s has stared eating.' % self.name)
                    t__.s..(5)

                    print('%s is now full.' % self.name)
                    self.hungry _ F..

fork _ ?.Lock()

partner1 _ Spouse('Wife', N..)
partner2 _ Spouse('Husband', partner1)
partner1.partner _ partner2

partner1.s..
partner2.s..

partner1.j..
partner2.j..

print('Finished.')

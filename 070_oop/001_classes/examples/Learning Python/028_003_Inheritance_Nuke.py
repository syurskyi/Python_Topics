import nuke


class Super:
    def method(self):
        nuke.tprint('#' * 23 + ' Default behavior')
        self.grade = nuke.createNode('Grade', inpanel=False)
        nuke.tprint('#' * 23 + ' in Super.method')

    def delegate(self):
        self.action()


class  Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        nuke.tprint('#' * 23 + ' Replace method completely')
        blur = nuke.createNode('Blur', inpanel=False)
        nuke.tprint('#' * 23 + ' in Replacer.method')


class Extender(Super):
    def method(self):
        nuke.tprint('#' * 23 + ' Extend method behavior')
        nuke.tprint('starting Extender.method')
        Super.method(self)
        self.grade['white'].setValue(5)
        nuke.tprint('ending Extender.method')

class Provider(Super):
    def action(self):
        nuke.tprint('#' * 23 + ' Fill in a required method')
        transform = nuke.createNode('Transform', inpanel=False)
        nuke.tprint('ending Provider.method')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()



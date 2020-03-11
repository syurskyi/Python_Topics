class Phone(object):
    def __init__(self):
        self.number = 1234567

    def call(self):
        print('call'), self.number

p = Phone()
p.call()

class Phone(object):
    def __init__(self):
        self.model = ''
        self.color = 'red'

    def call(self):
        print('call')

p = Phone()
p.call()
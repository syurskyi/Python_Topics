class Notation(object):
    steps = 0
    result = 0

    def __init__(self):
        pass

    def run(self):
        print("You need to implement run method to %s class." % type(self).__name__)
        pass

    def add_step(self):
        self.steps += 1

    def set_result(self, result):
        self.result = result

    def print_results(self):
        print("O(%s) - Steps: %d" % (type(self).__name__, self.steps))

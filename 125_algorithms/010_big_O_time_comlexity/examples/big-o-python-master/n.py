from notation import Notation

class N(Notation):

    def run(self, n):
        total = 0
        for x in range(1, n+1):
            self.add_step()
            total += x
        self.set_result(total)

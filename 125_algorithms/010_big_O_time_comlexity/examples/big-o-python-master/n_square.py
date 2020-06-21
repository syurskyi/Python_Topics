from notation import Notation

class NSquare(Notation):

    def run(self, n):
        total = 0
        for x in range(1, n+1):
            for y in range(1, n+1):
                self.add_step()
                total += (x + y)
        self.set_result(total)

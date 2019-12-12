from notation import Notation

class One(Notation):
    
    def run(self, n):
        self.add_step()
        result = n * (n + 1) / 2
        self.set_result(result)

from notation import Notation
import random

class LogN(Notation):

    def run(self, n):
        data_array = random.sample(range(1, 10000), n)
        data_array.sort()
        data_to_find = data_array[random.randint(0, len(data_array) -1)]

        l = 0
        h = len(data_array) -1
        while l <= h:
            m = int((l + h) / 2)
            self.add_step()
            if data_array[m] < data_to_find:
                l = m + 1
            elif data_array[m] > data_to_find:
                h = m - 1
            else:
                self.set_result(m)
                break

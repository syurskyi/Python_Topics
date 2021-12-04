____ ____


class AsyncIterator:

    ___ __init__(self, n):
        self.i = 0
        self.n = n

    ___ __aiter__(self):
        return self

    _____ ___ __anext__(self):
        print(f'start {self.i}')
        _____ ____.s..(1)
        print(f'end {self.i}')

        if self.i >= self.n:
            raise StopAsyncIteration
        self.i += 1
        return self.i


_____ ___ main():
    _____ for n in AsyncIterator(10):
        print(f'finally {n}')


__ _______ __ _______
    ____.run(main())

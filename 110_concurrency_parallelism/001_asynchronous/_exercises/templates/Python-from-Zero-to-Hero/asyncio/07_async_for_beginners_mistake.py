____ ____


c_ AsyncIterator:

    ___  -   n):
        i = 0
        n = n

    ___ __aiter__
        r_ self

    _____ ___ __anext__
        print(f'start {i}')
        _____ ____.s..(1)
        print(f'end {i}')

        __ i >= n:
            raise StopAsyncIteration
        i += 1
        r_ i


_____ ___ main
    _____ ___ n __ AsyncIterator(10):
        print(f'finally {n}')


__ _______ __ _______
    ____.run(main())

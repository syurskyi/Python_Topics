# ch18/example5.py

______ types

@types.coroutine
___ read_data():
    ___ inner(n):
        ___
            print(f'Printing from read_data(): {n}')
            callback _ gen.send(n * 2)
        ______ StopIteration:
            p..

    data _ yield inner
    r_ data

? ___ process():
    ___
        w__ T..:
            data _ ? read_data()
            print(f'Printing from process(): {data}')
    f..
        print('Processing done.')

gen _ process()
callback _ gen.send(N..)

___ main():
    ___ i __ ra..(5):
        print(f'Printing from main(): {i}')
        callback(i)

__ _______ __ _______
    main()

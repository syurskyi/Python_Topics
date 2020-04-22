# ch18/example4.py

___ read_data():
    ___ i __ ra..(5):
        print('Inside the inner for loop...')
        yield i * 2

result _ read_data()
___ i __ ra..(6):
    print('Inside the outer for loop...')
    print(next(result))

print('Finished.')

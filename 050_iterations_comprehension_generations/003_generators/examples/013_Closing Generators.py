# Closing Generators
# We can actually close a generator by sending it a special message, calling its close() method.

import csv

def parse_file(f_name):
    print('opening file...')
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)  # skip header row
        reader = csv.reader(f, dialect=dialect)
        for row in reader:
            try:
                yield row
            except GeneratorExit:
                print('got a close...')
                raise
    finally:
        print('cleaning up...')
        f.close()

parser = parse_file('cars.csv')
for row in itertools.islice(parser, 5):
    print(row)

parser.close()

# Closing Generators
#
# We can actually close a generator by sending it a special message, calling its close() method.

def parse_file(f_name):
    print('opening file...')
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)  # skip header row
        reader = csv.reader(f, dialect=dialect)
        for row in reader:
            try:
                yield row
            except GeneratorExit:
                print('got a close...')
                return
    finally:
        print('cleaning up...')
        f.close()

parser = parse_file('cars.csv')
for row in itertools.islice(parser, 5):
    print(row)

parser.close()

# Closing Generators
# def save_to_db()
# Notice how we're not even catching the GeneratorExit exception - we really don't need to -
# that exception will be raised, the finally block will run, and the GeneratorExit exception will be bubbled up to
# Python who will expect it after the call to close()

def save_to_db():
    print('starting new transaction')
    is_abort = False
    try:
        while True:
            data = yield
            print('sending data to database:', eval(data))
    except Exception:
        is_abort = True
        raise
    finally:
        if is_abort:
            print('aborting transaction')
        else:
            print('committing transaction')

trans = save_to_db()
next(trans)
trans.send('1 + 1')
trans.close()

trans = save_to_db()
next(trans)
trans.send('1 / 0')

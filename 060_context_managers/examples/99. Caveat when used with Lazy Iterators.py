print('#' * 52 + '  ### Caveat with Lazy Iterators')

import csv

def read_data():
    with open('nyc_parking_tickets_extract.csv') as f:
        return csv.reader(f, delimiter=',', quotechar='"')

# for row in read_data():
#     print(row)         # ValueError: I/O operation on closed file.


print('#' * 52 + '  The first one is not very desirable since it involves reading the entire file into memory'
                 '  by iterating the file and putting it into a list before we exit the `with` block:')

def read_data():
    with open('nyc_parking_tickets_extract.csv') as f:
        return list(csv.reader(f, delimiter=',', quotechar='"'))

for row in read_data():
    print(row)

print('#' * 52 + '  The second method, the one we have used quite a bit,'
                 '  involves yielding each row from the csv reader:')

def read_data():
    with open('nyc_parking_tickets_extract.csv') as f:
        yield from csv.reader(f, delimiter=',', quotechar='"')

for row in read_data():
    print(row)

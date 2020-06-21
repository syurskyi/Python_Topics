import csv

with open('data/example1.csv', 'r') as f:
    reader = csv.reader(f)
    print('Line nums', reader.line_num)
    print('Dialect', reader.dialect)
    for row in reader:
        print(row)

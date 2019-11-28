import csv

sniffer = csv.Sniffer()
dialect = None

with open('data/undefined_dialect.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('data/undefined_dialect.csv', 'r') as f:
    content = f.read()
    dialect = sniffer.sniff(content)

print(dialect.delimiter, dialect.doublequote, dialect.quoting)

with open('data/undefined_dialect.csv', 'r') as f:
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)

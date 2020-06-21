import csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "*"
    delimiter = "!"
    lineterminator = '\n'


csv.register_dialect('tester', CustomDialect)

with open('data/output.csv', 'w') as f:
    # writer = csv.writer(f, dialect=CustomDialect)
    writer = csv.writer(f, dialect='tester')
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])

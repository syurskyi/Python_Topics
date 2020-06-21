import csv

quoting = csv.QUOTE_ALL

with open('data/output.csv', 'w') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name', 'last_name', 'age'],
        quoting=quoting
    )

    writer.writeheader()
    writer.writerow({
        'first_name': 'Ivan',
        'last_name': 'Petrov @ ll, Test',
        'age': 20
    })
    writer.writerow({
        'first_name': 'Dmitry',
        'last_name': 'Sidorov',
        'age': 30
    })
    writer.writerow({
        'first_name': 'Alexey',
        'last_name': 'Ivanov',
        'age': 30
    })

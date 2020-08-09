#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ json
______ os
from collections ______ Counter


___ getFromJson(
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        r_ json.load(file)


__ __name__ __ "__main__":
    birthdays = getFromJson()
    values = list(birthdays.values())
    months = []
    ___ date in values:
        month = (date.split('.'))[1]
        months.append(month)

    yearMonths = {
        '01': 'January',
        '02': 'Februrary',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }

    count = Counter(months)
    ___ key in count.keys(
        print('In {} were {} guys'.format(yearMonths[key], count[key]))

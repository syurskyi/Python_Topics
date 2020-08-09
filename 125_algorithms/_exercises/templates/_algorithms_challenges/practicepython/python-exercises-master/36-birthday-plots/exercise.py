#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ json
______ os
from collections ______ Counter

from bokeh.plotting ______ figure, show, output_file

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


___ getFromJson(
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        r_ json.load(file)


___ formatDataToStringMonths(values
    months = []
    ___ date in values:
        month = (date.split('.'))[1]
        months.append(month)

    count = Counter(months)
    print(count)
    result = {}
    ___ key in count.keys(
        result[yearMonths[key]] = count[key]

    r_ result


___ printPlot(data
    output_file("plot.html")
    x_categories = list(yearMonths.values())
    x = list(data.keys())
    y = list(data.values())
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)
    show(p)

__ __name__ __ "__main__":
    birthdays = getFromJson()
    values = list(birthdays.values())
    data = formatDataToStringMonths(values)
    printPlot(data)

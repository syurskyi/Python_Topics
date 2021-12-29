import csv


def process_classes(classes: list) -> list:
    '''cleans and returns classes according to SIS as list'''
    return [cls.split(' - ')[0].replace('"', '') for cls in classes if cls]


def process_row(row):
    '''processes row according to SIS format.'''
    classes = process_classes(row[2:])
    return [','.join([cls, '2020', row[0]]) for cls in classes]


def class_rosters(input_file):
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    sis_list = list()
    with open(input_file, 'r') as f:
        for row in csv.reader(f):
            sis_rows = process_row(row)
            if sis_rows:
                sis_list.extend(sis_rows)
    return sis_list

import csv


def class_rosters(input_file):
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
     
    school_year = 2020 
    result = []
    with open(input_file,'r') as f:
        data = csv.reader(f)

        for row in data:
            _id = row[0]
            for i in range(2,len(row)):
                class_ = row[i]
                if class_:
                    class_section = class_.rsplit(' - ')[0]
                    result.append(f"{class_section},{school_year},{_id}")



    return result







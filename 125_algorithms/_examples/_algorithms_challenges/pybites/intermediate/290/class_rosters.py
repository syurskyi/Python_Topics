import csv
 

def class_rosters(input_file):
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    class_assignments = []
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            row_class_check = [class_d for class_d in row if class_d != ""]
            if len(row_class_check) > 2:
                student_id = row_class_check[0]
                for class_a in row_class_check[2:]:
                    class_name = class_a.split(" ")[0]
                    class_assignments.append(f"{class_name},2020,{student_id}")
    return class_assignments


# if __name__ == "__main__":
#     print(class_rosters("test.csv"))
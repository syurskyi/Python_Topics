_______ c__
 

___ class_rosters(input_file
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    class_assignments    # list
    w__ o.. input_file) __ csv_file:
        csv_reader c__.reader(csv_file)
        ___ row __ csv_reader:
            row_class_check [class_d ___ class_d __ row __ class_d !_ ""]
            __ l..(row_class_check) > 2:
                student_id row_class_check[0]
                ___ class_a __ row_class_check[2:]:
                    class_name class_a.s..(" ")[0]
                    class_assignments.a..(f"{class_name},2020,{student_id}")
    r.. class_assignments


# if __name__ == "__main__":
#     print(class_rosters("test.csv"))